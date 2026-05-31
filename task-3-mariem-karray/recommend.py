TOP_N = 5

CATALOG = [
    {"title": "Interstellar", "tags": ["Sci-Fi", "Drama", "Mystery"]},
    {"title": "The Dark Knight", "tags": ["Action", "Drama", "Thriller"]},
    {"title": "Superbad", "tags": ["Comedy"]},
    {"title": "Spirited Away", "tags": ["Anime", "Drama", "Mystery"]},
    {"title": "Whiplash", "tags": ["Drama", "Thriller"]},
    {"title": "Inception", "tags": ["Sci-Fi", "Action", "Thriller"]},
]


def clean_tag(tag):
    return tag.lower().strip()


def jaccard(user_tags, item_tags):
    user = {clean_tag(t) for t in user_tags if clean_tag(t)}
    item = {clean_tag(t) for t in item_tags if clean_tag(t)}
    if not user and not item:
        return 1.0
    if not user or not item:
        return 0.0
    return len(user & item) / len(user | item)


def get_recommendations(user_tags):
    scored = []
    for item in CATALOG:
        scored.append((item, jaccard(user_tags, item["tags"])))
    scored.sort(key=lambda row: row[1], reverse=True)
    return scored[:TOP_N]


def print_results(results):
    print("\n" + "=" * 50)
    print(f"TOP {TOP_N} RECOMMENDATIONS")
    print("=" * 50)
    for i, (item, score) in enumerate(results, start=1):
        print(f"\n#{i}  {item['title']}")
        print(f"    Score: {score * 100:.1f}%")
        print(f"    Tags:  {', '.join(item['tags'])}")
    print("\n" + "=" * 50 + "\n")


def run_demo():
    profile = ["sci-fi", "thriller", "action"]
    print("Test profile:", ", ".join(profile))
    results = get_recommendations(profile)
    print_results(results)
    if results[0][0]["title"] == "Inception":
        print("PASS")
    else:
        print("FAIL")


def main():
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
        return

    raw = input("Enter tags (comma-separated): ").strip()
    if not raw:
        print("No tags entered.")
        return

    user_tags = [clean_tag(part) for part in raw.split(",") if clean_tag(part)]
    print_results(get_recommendations(user_tags))


if __name__ == "__main__":
    main()
