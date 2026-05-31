const DATABASE = {
  movies: [
    {
      id: "m1",
      title: "Interstellar",
      desc: "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
      tags: ["Sci-Fi", "Drama", "Mystery"],
      attributes: { pacing: 0.6, depth: 0.9, emotion: 0.9, complexity: 0.8 }
    },
    {
      id: "m2",
      title: "The Dark Knight",
      desc: "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
      tags: ["Action", "Drama", "Thriller"],
      attributes: { pacing: 0.8, depth: 0.7, emotion: 0.6, complexity: 0.5 }
    },
    {
      id: "m3",
      title: "Superbad",
      desc: "Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.",
      tags: ["Comedy"],
      attributes: { pacing: 0.8, depth: 0.2, emotion: 0.4, complexity: 0.2 }
    },
    {
      id: "m4",
      title: "Spirited Away",
      desc: "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts.",
      tags: ["Anime", "Drama", "Mystery"],
      attributes: { pacing: 0.5, depth: 0.9, emotion: 0.8, complexity: 0.7 }
    },
    {
      id: "m5",
      title: "Whiplash",
      desc: "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
      tags: ["Drama", "Thriller"],
      attributes: { pacing: 0.9, depth: 0.8, emotion: 0.8, complexity: 0.6 }
    },
    {
      id: "m6",
      title: "Inception",
      desc: "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
      tags: ["Sci-Fi", "Action", "Thriller"],
      attributes: { pacing: 0.8, depth: 0.8, emotion: 0.6, complexity: 0.9 }
    }
  ],
  books: [
    {
      id: "b1",
      title: "Dune",
      desc: "Set on the desert planet Arrakis, a mythical sweep of political intrigues, giant sandworms, and high sci-fi mysticism.",
      tags: ["Sci-Fi", "Fantasy", "Classic"],
      attributes: { pacing: 0.5, depth: 0.9, emotion: 0.5, complexity: 0.9 }
    },
    {
      id: "b2",
      title: "The Hobbit",
      desc: "A quiet hobbit named Bilbo Baggins is whisked away into a magical, epic quest to reclaim a lost treasure from a dragon.",
      tags: ["Fantasy", "Classic"],
      attributes: { pacing: 0.7, depth: 0.6, emotion: 0.7, complexity: 0.5 }
    },
    {
      id: "b3",
      title: "Sherlock Holmes: A Study in Scarlet",
      desc: "The famous meeting between Watson and Holmes, followed by a fascinating investigation into a mysterious murder.",
      tags: ["Mystery", "Classic"],
      attributes: { pacing: 0.8, depth: 0.5, emotion: 0.3, complexity: 0.7 }
    },
    {
      id: "b4",
      title: "Pride and Prejudice",
      desc: "Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy in this timeless comedy of manners.",
      tags: ["Romance", "Classic", "Drama"],
      attributes: { pacing: 0.4, depth: 0.7, emotion: 0.8, complexity: 0.5 }
    },
    {
      id: "b5",
      title: "Project Hail Mary",
      desc: "A sole surviving astronaut must use his scientific wits to save Earth from an extinction-level event, accompanied by a friendly alien.",
      tags: ["Sci-Fi", "Mystery"],
      attributes: { pacing: 0.8, depth: 0.7, emotion: 0.8, complexity: 0.6 }
    }
  ],
  games: [
    {
      id: "g1",
      title: "Elden Ring",
      desc: "Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
      tags: ["RPG", "Action"],
      attributes: { pacing: 0.6, difficulty: 0.9, length: 0.9, complexity: 0.8 }
    },
    {
      id: "g2",
      title: "Portal 2",
      desc: "Solve innovative physics puzzles using a portal device while surviving a humorous but sinister artificial intelligence.",
      tags: ["Puzzle", "Sci-Fi"],
      attributes: { pacing: 0.5, difficulty: 0.5, length: 0.4, complexity: 0.7 }
    },
    {
      id: "g3",
      title: "Stardew Valley",
      desc: "Inherit your grandfather's old farm plot, raise livestock, grow crops, and integrate into the local cozy community.",
      tags: ["Indie", "Cozy"],
      attributes: { pacing: 0.3, difficulty: 0.2, length: 0.8, complexity: 0.5 }
    },
    {
      id: "g4",
      title: "Cyberpunk 2077",
      desc: "An open-world, action-adventure RPG set in Night City, a megalopolis obsessed with power, glamour and body modification.",
      tags: ["RPG", "Action", "Sci-Fi"],
      attributes: { pacing: 0.8, difficulty: 0.5, length: 0.7, complexity: 0.7 }
    },
    {
      id: "g5",
      title: "Doom Eternal",
      desc: "Hell's armies have invaded Earth. Become the Slayer in an epic single-player campaign to conquer demons across dimensions.",
      tags: ["Action", "Shooter"],
      attributes: { pacing: 0.9, difficulty: 0.8, length: 0.5, complexity: 0.4 }
    }
  ],
  travel: [
    {
      id: "t1",
      title: "Tokyo, Japan",
      desc: "A sprawling metropolis combining futuristic neon skyscrapers, historic temples, pop culture, and world-class culinary art.",
      tags: ["City", "Culture", "Culinary"],
      attributes: { cost: 0.8, adventure: 0.5, crowds: 0.8, nature: 0.3 }
    },
    {
      id: "t2",
      title: "Swiss Alps",
      desc: "A breathtaking alpine paradise perfect for clean air, hiking, majestic snowy peaks, ski resorts, and peaceful mountain chalets.",
      tags: ["Nature", "Adventure"],
      attributes: { cost: 0.9, adventure: 0.7, crowds: 0.4, nature: 0.9 }
    },
    {
      id: "t3",
      title: "Bali, Indonesia",
      desc: "An exotic tropical haven known for forested volcanic mountains, iconic rice paddies, beaches, temples, and yoga retreats.",
      tags: ["Nature", "Relaxation", "Beach"],
      attributes: { cost: 0.4, adventure: 0.6, crowds: 0.6, nature: 0.8 }
    },
    {
      id: "t4",
      title: "Paris, France",
      desc: "A global center for art, fashion, gastronomy, and culture, defined by romantic riverfronts and 19th-century charm.",
      tags: ["City", "Art", "Culinary"],
      attributes: { cost: 0.8, adventure: 0.3, crowds: 0.9, nature: 0.3 }
    },
    {
      id: "t5",
      title: "Costa Rica Wilderness",
      desc: "A rugged, rainforested Central American country with coastlines on the Caribbean and Pacific, famous for biodiversity.",
      tags: ["Nature", "Adventure", "Beach"],
      attributes: { cost: 0.5, adventure: 0.8, crowds: 0.5, nature: 0.9 }
    }
  ]
};

const SCHEMAS = {
  movies: {
    tags: ["Action", "Sci-Fi", "Drama", "Comedy", "Romance", "Mystery", "Thriller", "Anime"],
    attributes: [
      { key: "pacing", name: "Pacing (Slow → Fast)" },
      { key: "depth", name: "Depth (Light → Deep)" },
      { key: "emotion", name: "Emotional Scale (Dry → Intense)" },
      { key: "complexity", name: "Complexity (Simple → Mind-bending)" }
    ]
  },
  books: {
    tags: ["Sci-Fi", "Fantasy", "Mystery", "Romance", "Thriller", "Drama", "Classic"],
    attributes: [
      { key: "pacing", name: "Pacing (Slow → Fast)" },
      { key: "depth", name: "Depth (Light → Deep)" },
      { key: "emotion", name: "Emotional Scale (Dry → Heartwarming)" },
      { key: "complexity", name: "Complexity (Simple → Multi-layered)" }
    ]
  },
  games: {
    tags: ["RPG", "Action", "Shooter", "Indie", "Puzzle", "Cozy", "Strategy"],
    attributes: [
      { key: "pacing", name: "Pacing (Slow → Intense)" },
      { key: "difficulty", name: "Difficulty (Casual → Hardcore)" },
      { key: "length", name: "Game Length (Short → Endless)" },
      { key: "complexity", name: "Complexity (Simple → Highly Strategic)" }
    ]
  },
  travel: {
    tags: ["City", "Nature", "Beach", "Culture", "Culinary", "Adventure", "Relaxation", "Art"],
    attributes: [
      { key: "cost", name: "Budget Required (Budget → Luxury)" },
      { key: "adventure", name: "Adventure Level (Mild → Extreme)" },
      { key: "crowds", name: "Crowd Density (Quiet → Bustling)" },
      { key: "nature", name: "Natural vs. Built (Urban → Wilderness)" }
    ]
  }
};

const TOP_N = 5;

let currentDomain = "movies";
const userPreferences = {
  tags: new Set(),
  attributes: {}
};

function normalizeTag(tag) {
  return tag.toLowerCase().trim();
}

function normalizeTagSet(tagIterable) {
  return new Set([...tagIterable].map(normalizeTag).filter((t) => t.length > 0));
}

const tagsContainer = document.getElementById("tags-container");
const slidersContainer = document.getElementById("sliders-container");
const recommendationsGrid = document.getElementById("recommendations-grid");
const jaccardWeightInput = document.getElementById("jaccard-weight");
const jaccardWeightVal = document.getElementById("jaccard-weight-val");
const euclideanWeightInput = document.getElementById("euclidean-weight");
const euclideanWeightVal = document.getElementById("euclidean-weight-val");
const sortSelect = document.getElementById("sort-select");
const recCountText = document.getElementById("recommendation-count");
const tabButtons = document.querySelectorAll(".tab-btn");

const sandboxToggle = document.getElementById("sandbox-toggle");
const sandboxFormContainer = document.getElementById("sandbox-form-container");
const customItemForm = document.getElementById("custom-item-form");
const sandboxSliders = document.getElementById("sandbox-sliders");

function init() {
  setupTabs();
  setupWeightControllers();
  setupSandboxToggle();
  setupThemeToggle();
  loadDomain(currentDomain);

  customItemForm.addEventListener("submit", handleCustomItemSubmit);
  sortSelect.addEventListener("change", renderRecommendations);
}

function setupThemeToggle() {
  const toggleBtn = document.getElementById("theme-toggle-btn");

  const savedTheme = localStorage.getItem("app-theme") || "light";
  document.body.setAttribute("data-theme", savedTheme);

  toggleBtn.addEventListener("click", () => {
    const currentTheme = document.body.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    document.body.setAttribute("data-theme", newTheme);
    localStorage.setItem("app-theme", newTheme);
  });
}

function loadDomain(domain) {
  currentDomain = domain;

  userPreferences.tags.clear();
  userPreferences.attributes = {};

  SCHEMAS[domain].attributes.forEach(attr => {
    userPreferences.attributes[attr.key] = 0.5;
  });

  renderControls(domain);
  renderSandboxSliders(domain);
  renderRecommendations();
}

function setupTabs() {
  tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      tabButtons.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      loadDomain(btn.dataset.domain);
    });
  });
}

function setupWeightControllers() {
  jaccardWeightInput.addEventListener("input", (e) => {
    const val = parseInt(e.target.value);
    jaccardWeightVal.textContent = val + "%";
    euclideanWeightInput.value = 100 - val;
    euclideanWeightVal.textContent = (100 - val) + "%";
    renderRecommendations();
  });

  euclideanWeightInput.addEventListener("input", (e) => {
    const val = parseInt(e.target.value);
    euclideanWeightVal.textContent = val + "%";
    jaccardWeightInput.value = 100 - val;
    jaccardWeightVal.textContent = (100 - val) + "%";
    renderRecommendations();
  });
}

function setupSandboxToggle() {
  sandboxToggle.addEventListener("click", () => {
    sandboxFormContainer.classList.toggle("collapsed");
    const icon = sandboxToggle.querySelector(".toggle-icon");
    if (sandboxFormContainer.classList.contains("collapsed")) {
      icon.textContent = "▼";
    } else {
      icon.textContent = "▲";
    }
  });
}

function renderControls(domain) {
  tagsContainer.innerHTML = "";
  SCHEMAS[domain].tags.forEach(tag => {
    const pill = document.createElement("button");
    pill.className = "interest-tag";
    pill.textContent = tag;
    pill.addEventListener("click", () => {
      if (userPreferences.tags.has(tag)) {
        userPreferences.tags.delete(tag);
        pill.classList.remove("active");
      } else {
        userPreferences.tags.add(tag);
        pill.classList.add("active");
      }
      renderRecommendations();
    });
    tagsContainer.appendChild(pill);
  });

  slidersContainer.innerHTML = "";
  SCHEMAS[domain].attributes.forEach(attr => {
    const group = document.createElement("div");
    group.className = "slider-group";

    group.innerHTML = `
      <div class="slider-header">
        <span class="slider-name">${attr.name}</span>
        <span class="slider-val-bubble" id="pref-val-${attr.key}">50%</span>
      </div>
      <input type="range" min="0" max="100" value="50" class="custom-slider" data-key="${attr.key}">
    `;

    const slider = group.querySelector("input");
    slider.addEventListener("input", (e) => {
      const val = parseInt(e.target.value);
      userPreferences.attributes[attr.key] = val / 100;
      document.getElementById(`pref-val-${attr.key}`).textContent = val + "%";
      renderRecommendations();
    });

    slidersContainer.appendChild(group);
  });
}

function renderSandboxSliders(domain) {
  sandboxSliders.innerHTML = "";
  SCHEMAS[domain].attributes.forEach(attr => {
    const group = document.createElement("div");
    group.className = "form-group";
    group.innerHTML = `
      <label for="sandbox-val-${attr.key}">${attr.name}</label>
      <div style="display: flex; align-items: center; gap: 0.8rem;">
        <input type="range" id="sandbox-val-${attr.key}" min="0" max="100" value="50" class="custom-slider" style="flex: 1;">
        <span style="font-size: 0.8rem; font-family: var(--font-display); width: 32px; text-align: right;" id="sandbox-bubble-${attr.key}">50%</span>
      </div>
    `;

    const slider = group.querySelector("input");
    slider.addEventListener("input", (e) => {
      document.getElementById(`sandbox-bubble-${attr.key}`).textContent = e.target.value + "%";
    });
    sandboxSliders.appendChild(group);
  });
}

function handleCustomItemSubmit(e) {
  e.preventDefault();

  const title = document.getElementById("item-title").value.trim();
  const desc = document.getElementById("item-desc").value.trim();
  const rawTags = document.getElementById("item-tags").value;

  const tagsList = rawTags
    .split(",")
    .map((t) => normalizeTag(t))
    .filter((t) => t.length > 0);

  const attributes = {};
  SCHEMAS[currentDomain].attributes.forEach(attr => {
    const val = parseInt(document.getElementById(`sandbox-val-${attr.key}`).value);
    attributes[attr.key] = val / 100;
  });

  const newItem = {
    id: currentDomain[0] + (DATABASE[currentDomain].length + 1),
    title,
    desc,
    tags: tagsList,
    attributes
  };

  DATABASE[currentDomain].push(newItem);

  customItemForm.reset();
  SCHEMAS[currentDomain].attributes.forEach(attr => {
    document.getElementById(`sandbox-bubble-${attr.key}`).textContent = "50%";
  });

  alert(`✨ ${title} has been successfully loaded into the AI dataset! Calculation engine is re-running...`);

  renderRecommendations();
}

function jaccardScore(userTagSet, itemTagSet) {
  if (userTagSet.size === 0 && itemTagSet.size === 0) return 1.0;
  if (userTagSet.size === 0 || itemTagSet.size === 0) return 0.0;
  const intersection = [...userTagSet].filter((tag) => itemTagSet.has(tag)).length;
  const union = new Set([...userTagSet, ...itemTagSet]).size;
  return intersection / union;
}

function computeScores() {
  const dataset = DATABASE[currentDomain];
  const results = [];
  const userTagSet = normalizeTagSet(userPreferences.tags);
  const jaccardWeight = parseInt(jaccardWeightInput.value) / 100;
  const euclideanWeight = parseInt(euclideanWeightInput.value) / 100;
  const attrs = SCHEMAS[currentDomain].attributes;

  dataset.forEach((item) => {
    const itemTagSet = normalizeTagSet(item.tags);
    const tagScore = jaccardScore(userTagSet, itemTagSet);

    let sumSquaredDiff = 0;
    attrs.forEach((attr) => {
      const userVal = userPreferences.attributes[attr.key] || 0.5;
      const itemVal = item.attributes[attr.key] || 0;
      sumSquaredDiff += Math.pow(userVal - itemVal, 2);
    });

    const maxDist = Math.sqrt(attrs.length);
    const attrScore = 1 - Math.sqrt(sumSquaredDiff) / maxDist;
    const totalWeight = jaccardWeight + euclideanWeight;
    const overallScore = totalWeight > 0
      ? (tagScore * jaccardWeight + attrScore * euclideanWeight) / totalWeight
      : 0;

    results.push({ item, jaccardScore: tagScore, euclideanScore: attrScore, overallScore });
  });

  return results;
}

function renderRecommendations() {
  const scoredData = computeScores();
  const sortBy = sortSelect.value;

  scoredData.sort((a, b) => {
    if (sortBy === "jaccard") return b.jaccardScore - a.jaccardScore;
    if (sortBy === "distance") return b.euclideanScore - a.euclideanScore;
    return b.overallScore - a.overallScore;
  });

  const displayData = scoredData.slice(0, TOP_N);
  recCountText.textContent = `Top ${displayData.length} of ${scoredData.length} items by similarity score.`;

  recommendationsGrid.innerHTML = "";

  displayData.forEach(({ item, jaccardScore, euclideanScore, overallScore }) => {
    const card = document.createElement("div");
    const matchPct = Math.round(overallScore * 100);

    card.className = `rec-card ${matchPct >= 75 ? 'high-match' : ''}`;

    let tagsHTML = "";
    item.tags.forEach(tag => {
      const isMatched = normalizeTagSet(userPreferences.tags).has(normalizeTag(tag));
      tagsHTML += `<span class="card-tag-pill ${isMatched ? 'matched' : ''}">${tag}</span>`;
    });

    let attrsHTML = "";
    SCHEMAS[currentDomain].attributes.forEach(attr => {
      const val = item.attributes[attr.key] || 0;
      const userVal = userPreferences.attributes[attr.key] || 0.5;
      const isClose = Math.abs(val - userVal) <= 0.15;

      attrsHTML += `
        <div class="card-attr-item">
          <div class="card-attr-name">${attr.name.split(" ")[0]} (${Math.round(val * 100)}%)</div>
          <div class="card-attr-bar-outer">
            <div class="card-attr-bar-inner ${isClose ? 'aligned' : ''}" style="width: ${val * 100}%"></div>
          </div>
        </div>
      `;
    });

    const explanationText = generateExplanation(item, jaccardScore, euclideanScore);

    card.innerHTML = `
      <div class="match-badge">${matchPct}% Match</div>
      <div class="rec-header">
        <h3>${item.title}</h3>
      </div>
      <p class="rec-desc">${item.desc}</p>
      <div class="card-tags">
        ${tagsHTML}
      </div>
      <div class="card-attributes">
        ${attrsHTML}
      </div>
      <div class="rec-explainer">
        <button class="explainer-toggle">💡 Show Match Breakdown</button>
        <div class="explainer-body">
          ${explanationText}
        </div>
      </div>
    `;

    const toggleBtn = card.querySelector(".explainer-toggle");
    const body = card.querySelector(".explainer-body");
    toggleBtn.addEventListener("click", () => {
      body.classList.toggle("open");
      toggleBtn.textContent = body.classList.contains("open") ? "💡 Hide Match Breakdown" : "💡 Show Match Breakdown";
    });

    recommendationsGrid.appendChild(card);
  });
}

function generateExplanation(item, jaccardScore, euclideanScore) {
  const matched = item.tags.filter((t) =>
    normalizeTagSet(userPreferences.tags).has(normalizeTag(t))
  );
  const matchedText = matched.length ? matched.join(", ") : "none";
  return `
    <ul>
      <li>Matched tags: <strong>${matchedText}</strong></li>
      <li>Jaccard score: <strong>${Math.round(jaccardScore * 100)}%</strong></li>
      <li>Attribute score: <strong>${Math.round(euclideanScore * 100)}%</strong></li>
    </ul>
  `;
}

window.addEventListener("DOMContentLoaded", init);
