import json
import csv
import os

def main():
    csv_path = "iris.csv"
    if not os.path.exists(csv_path):
        print(f"Error: Could not find '{csv_path}'. Please run prepare_data.py first.")
        return

    # Parse iris.csv
    dataset = []
    with open(csv_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dataset.append({
                "sl": float(row['sepal_length_cm']),
                "sw": float(row['sepal_width_cm']),
                "pl": float(row['petal_length_cm']),
                "pw": float(row['petal_width_cm']),
                "sp": row['species'].strip().lower()
            })

    dataset_json = json.dumps(dataset, indent=2)

    # Generate chatbot.html
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IrisBot 🌸 - Premium Iris Flower Classifier</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #eef2f7;
            --primary: #7c3aed;
            --primary-glow: rgba(124, 58, 237, 0.14);
            --secondary: #db2777;
            --secondary-glow: rgba(219, 39, 119, 0.12);
            --accent: #059669;
            --accent-glow: rgba(5, 150, 105, 0.12);
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(0, 0, 0, 0.08);
            --text-main: #111827;
            --text-muted: #6b7280;
            --bot-bubble: #ffffff;
            --user-bubble: linear-gradient(135deg, #6366f1, #a855f7);
            --surface-muted: #f8fafc;
            --header-bg: #ffffff;
            --input-bg: #f1f5f9;
            --font-outfit: 'Outfit', sans-serif;
            --font-inter: 'Inter', sans-serif;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-inter);
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        /* Radiant mesh background gradients */
        .bg-glow-1 {
            position: absolute;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            background: radial-gradient(circle, var(--primary-glow) 0%, transparent 70%);
            top: -10%;
            left: -10%;
            z-index: 1;
            filter: blur(80px);
            animation: floatGlow 15s infinite alternate ease-in-out;
        }

        .bg-glow-2 {
            position: absolute;
            width: 600px;
            height: 600px;
            border-radius: 50%;
            background: radial-gradient(circle, var(--secondary-glow) 0%, transparent 70%);
            bottom: -15%;
            right: -10%;
            z-index: 1;
            filter: blur(100px);
            animation: floatGlow 20s infinite alternate-reverse ease-in-out;
        }

        @keyframes floatGlow {
            0% { transform: translate(0, 0) scale(1); }
            100% { transform: translate(50px, 30px) scale(1.1); }
        }

        /* App Container */
        .app-container {
            width: 100%;
            max-width: 600px;
            height: 85vh;
            max-height: 800px;
            border-radius: 24px;
            background: var(--glass-bg);
            backdrop-filter: blur(20px) saturate(180%);
            -webkit-backdrop-filter: blur(20px) saturate(180%);
            border: 1px solid var(--glass-border);
            z-index: 10;
            display: flex;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.12);
            overflow: hidden;
            transition: all 0.3s ease;
        }

        @media (max-width: 768px) {
            .app-container {
                height: 100vh;
                max-height: 100vh;
                border-radius: 0;
                border: none;
            }
        }


        /* Chat Panel */
        .chat-panel {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: var(--surface-muted);
            height: 100%;
        }

        /* Chat Header */
        .chat-header {
            padding: 20px 30px;
            border-bottom: 1px solid var(--glass-border);
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--header-bg);
        }

        .bot-profile {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .bot-avatar {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            background: linear-gradient(135deg, #7c3aed, #db2777);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
            position: relative;
        }

        .bot-status-dot {
            position: absolute;
            bottom: 0;
            right: 0;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: var(--accent);
            border: 2px solid #ffffff;
            box-shadow: 0 0 8px var(--accent);
        }

        .bot-meta h2 {
            font-family: var(--font-outfit);
            font-size: 16px;
            font-weight: 600;
        }

        .bot-meta p {
            font-size: 12px;
            color: var(--accent);
            font-weight: 500;
        }

        .action-icon-btn {
            background: #ffffff;
            border: 1px solid var(--glass-border);
            color: var(--text-main);
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .action-icon-btn:hover {
            background: var(--input-bg);
            transform: scale(1.05);
        }

        /* Chat messages list */
        .chat-messages {
            flex: 1;
            padding: 30px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 20px;
            scroll-behavior: smooth;
        }

        /* Scrollbar customization */
        .chat-messages::-webkit-scrollbar {
            width: 6px;
        }
        .chat-messages::-webkit-scrollbar-track {
            background: transparent;
        }
        .chat-messages::-webkit-scrollbar-thumb {
            background: rgba(0, 0, 0, 0.15);
            border-radius: 10px;
        }
        .chat-messages::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 0, 0, 0.25);
        }


        .message-row {
            display: flex;
            width: 100%;
        }

        .message-row.bot {
            justify-content: flex-start;
        }

        .message-row.user {
            justify-content: flex-end;
        }

        .message-bubble {
            max-width: 75%;
            padding: 14px 18px;
            border-radius: 18px;
            font-size: 14px;
            line-height: 1.5;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
            animation: fadeInUp 0.3s ease forwards;
            opacity: 0;
            transform: translateY(15px);
        }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .bot .message-bubble {
            background: var(--bot-bubble);
            border: 1px solid var(--glass-border);
            border-top-left-radius: 4px;
            color: var(--text-main);
        }

        .user .message-bubble {
            background: var(--user-bubble);
            border-top-right-radius: 4px;
            color: #ffffff;
        }

        /* Quick Action Chips */
        .chips-container {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 10px;
            animation: fadeInUp 0.3s ease 0.1s forwards;
            opacity: 0;
        }

        .chip-btn {
            background: rgba(124, 58, 237, 0.08);
            border: 1px solid rgba(124, 58, 237, 0.2);
            color: #6d28d9;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .chip-btn:hover {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            transform: translateY(-2px);
            box-shadow: 0 4px 12px var(--primary-glow);
        }

        /* Sliding Card Form */
        .slider-card {
            background: #ffffff;
            border: 1px solid var(--glass-border);
            border-radius: 20px;
            padding: 24px;
            width: 100%;
            max-width: 420px;
            margin-top: 12px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08);
            animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        .slider-title {
            font-family: var(--font-outfit);
            font-size: 16px;
            font-weight: 600;
            margin-bottom: 20px;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .slider-group {
            margin-bottom: 18px;
        }

        .slider-group:last-of-type {
            margin-bottom: 24px;
        }

        .slider-header {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            margin-bottom: 8px;
            color: var(--text-muted);
        }

        .slider-label {
            font-weight: 500;
            color: var(--text-main);
        }

        .slider-value {
            font-family: var(--font-outfit);
            font-weight: 600;
            color: var(--secondary);
            background: rgba(236, 72, 153, 0.1);
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 12px;
        }

        input[type="range"] {
            -webkit-appearance: none;
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: #e2e8f0;
            outline: none;
            transition: all 0.2s ease;
        }

        input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border-radius: 50%;
            background: linear-gradient(135deg, #a855f7, #ec4899);
            cursor: pointer;
            box-shadow: 0 0 8px rgba(168, 85, 247, 0.5);
            transition: all 0.2s ease;
        }

        input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.2);
            box-shadow: 0 0 12px rgba(168, 85, 247, 0.8);
        }

        .predict-btn {
            width: 100%;
            padding: 12px 20px;
            background: linear-gradient(135deg, #7c3aed, #db2777);
            border: none;
            border-radius: 12px;
            color: #ffffff;
            font-family: var(--font-outfit);
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .predict-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5);
        }

        /* Prediction Result Card */
        .result-card {
            border-radius: 20px;
            padding: 24px;
            width: 100%;
            max-width: 420px;
            margin-top: 15px;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
            animation: fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            position: relative;
            overflow: hidden;
        }

        .result-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.6) 0%, transparent 60%);
            pointer-events: none;
        }

        .result-card.setosa {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
            border: 1px solid rgba(99, 102, 241, 0.3);
        }

        .result-card.versicolor {
            background: linear-gradient(135deg, rgba(236, 72, 153, 0.15), rgba(168, 85, 247, 0.15));
            border: 1px solid rgba(236, 72, 153, 0.3);
        }

        .result-card.virginica {
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(99, 102, 241, 0.15));
            border: 1px solid rgba(16, 185, 129, 0.3);
        }

        .result-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 15px;
        }

        .result-species {
            font-family: var(--font-outfit);
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        .setosa .result-species { color: #4f46e5; }
        .versicolor .result-species { color: #db2777; }
        .virginica .result-species { color: #059669; }

        .species-avatar {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }

        .setosa .species-avatar { background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.3); }
        .versicolor .species-avatar { background: rgba(236, 72, 153, 0.2); border: 1px solid rgba(236, 72, 153, 0.3); }
        .virginica .species-avatar { background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.3); }

        .result-desc {
            font-size: 13.5px;
            line-height: 1.6;
            color: var(--text-muted);
            margin-bottom: 20px;
        }

        .result-metrics {
            border-top: 1px solid var(--glass-border);
            padding-top: 15px;
        }

        .metric-title {
            font-family: var(--font-outfit);
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--text-muted);
            margin-bottom: 10px;
        }

        .metric-row {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .metric-item {
            background: var(--surface-muted);
            border: 1px solid var(--glass-border);
            border-radius: 8px;
            padding: 8px 12px;
            font-size: 12px;
            color: var(--text-muted);
        }

        .metric-item strong {
            color: var(--text-main);
            font-weight: 500;
            display: block;
            margin-top: 2px;
        }

        /* Typing Indicator Bubble */
        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 5px;
            padding: 10px 15px;
            background: var(--bot-bubble);
            border: 1px solid var(--glass-border);
            border-radius: 18px;
            border-top-left-radius: 4px;
            width: fit-content;
            animation: fadeInUp 0.2s ease forwards;
        }

        .typing-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--text-muted);
            animation: typingBounce 1.4s infinite ease-in-out both;
        }

        .typing-dot:nth-child(1) { animation-delay: 0s; }
        .typing-dot:nth-child(2) { animation-delay: 0.2s; }
        .typing-dot:nth-child(3) { animation-delay: 0.4s; }

        @keyframes typingBounce {
            0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
            40% { transform: scale(1); opacity: 1; }
        }

        /* Chat Input Section */
        .chat-input-area {
            padding: 24px 30px;
            border-top: 1px solid var(--glass-border);
            background: #ffffff;
            position: relative;
        }

        .chat-form {
            display: flex;
            align-items: center;
            gap: 12px;
            width: 100%;
        }

        .input-wrapper {
            position: relative;
            flex: 1;
        }

        .chat-input {
            width: 100%;
            padding: 14px 20px;
            padding-right: 50px;
            background: var(--input-bg);
            border: 1px solid var(--glass-border);
            border-radius: 14px;
            color: var(--text-main);
            font-size: 14px;
            outline: none;
            transition: all 0.2s ease;
        }

        .chat-input:focus {
            border-color: var(--primary);
            background: #ffffff;
            box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15);
        }

        .chat-input::placeholder {
            color: var(--text-muted);
        }

        .input-icon {
            position: absolute;
            right: 18px;
            top: 50%;
            transform: translateY(-50%);
            font-size: 18px;
            color: var(--text-muted);
            pointer-events: none;
        }

        .send-btn {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            border: none;
            background: linear-gradient(135deg, #7c3aed, #db2777);
            color: #ffffff;
            font-size: 18px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);
        }

        .send-btn:hover {
            transform: scale(1.05) translateY(-1px);
            box-shadow: 0 6px 16px rgba(124, 58, 237, 0.5);
        }

        .send-btn:active {
            transform: scale(0.95);
        }
    </style>
</head>
<body>
    <div class="bg-glow-1"></div>
    <div class="bg-glow-2"></div>
    <div class="app-container">
        <!-- Main Chat Panel -->
        <main class="chat-panel">
            <!-- Header -->
            <header class="chat-header">
                <div class="bot-profile">
                    <div class="bot-avatar">
                        🌸
                        <div class="bot-status-dot"></div>
                    </div>
                    <div class="bot-meta">
                        <h2>IrisBot</h2>
                        <p>Online • AI Botanist</p>
                    </div>
                </div>
                <div class="action-icon-btn" onclick="resetChat()" title="Reset Conversation">
                    🔄
                </div>
            </header>

            <!-- Chat messages -->
            <div class="chat-messages" id="chatMessages">
                <!-- Greeting message will be inserted dynamically -->
            </div>

            <!-- Input area -->
            <div class="chat-input-area">
                <form class="chat-form" id="chatForm" onsubmit="handleFormSubmit(event)">
                    <div class="input-wrapper">
                        <input type="text" class="chat-input" id="chatInput" placeholder="Message IrisBot..." autocomplete="off">
                        <span class="input-icon">💬</span>
                    </div>
                    <button class="send-btn" type="submit" id="sendBtn">
                        ➡️
                    </button>
                </form>
            </div>
        </main>
    </div>

    <script>
        // The complete Iris dataset parsed dynamically from iris.csv
        const irisDataset = {dataset_json};

        // State management for step-by-step chatbot classification
        const STATE_CHAT = "chat";
        const STATE_ASK_SL = "ask_sl";
        const STATE_ASK_SW = "ask_sw";
        const STATE_ASK_PL = "ask_pl";
        const STATE_ASK_PW = "ask_pw";

        let currentConversationState = STATE_CHAT;
        let flowMeasurements = {
            sl: null,
            sw: null,
            pl: null,
            pw: null
        };

        // Botanist descriptive text for the result cards
        const speciesDetails = {
            setosa: {
                title: "Iris Setosa",
                emoji: "💐",
                desc: "Known as the wild flag iris, Setosa has exceptionally small petals relative to its large sepals. It is native to the Arctic and sub-Arctic regions of North America and East Asia, thriving in marshy areas.",
                sl: "4.3 - 5.8 cm",
                sw: "2.3 - 4.4 cm",
                pl: "1.0 - 1.9 cm",
                pw: "0.1 - 0.6 cm"
            },
            versicolor: {
                title: "Iris Versicolor",
                emoji: "🌺",
                desc: "Commonly known as the blue flag, Versicolor is the official state flower of Maine. It exhibits beautifully balanced measurements and is native to marshes, fens, and wet meadows of Eastern North America.",
                sl: "4.9 - 7.0 cm",
                sw: "2.0 - 3.4 cm",
                pl: "3.0 - 5.1 cm",
                pw: "1.0 - 1.8 cm"
            },
            virginica: {
                title: "Iris Virginica",
                emoji: "🌻",
                desc: "The Virginia iris has robust, broad petals and thick foliage. It is native to the coastal plains of the southeastern United States, showcasing the largest overall petal lengths and widths in the Iris family.",
                sl: "4.9 - 7.9 cm",
                sw: "2.2 - 3.8 cm",
                pl: "4.5 - 6.9 cm",
                pw: "1.4 - 2.5 cm"
            }
        };

        // Initialize Chat on Page Load
        window.addEventListener("DOMContentLoaded", () => {
            addBotMessage("Hello! I am **IrisBot** 🌸, your AI botanist assistant. I can help you identify Iris flower species in real-time based on their measurements.");
            showWelcomeOptions();
        });

        function showWelcomeOptions() {
            addBotOptions([
                { text: "🌸 Interactive Sliders", action: "open_sliders" },
                { text: "💬 Step-by-Step Chat", action: "start_chat_flow" },
                { text: "ℹ️ Species Catalog", action: "explain_species" }
            ]);
        }

        // Main chatbot responses routing
        function handleUserMessage(text) {
            const query = text.trim().toLowerCase();
            
            // If in active step-by-step measurement prompt state
            if (currentConversationState !== STATE_CHAT) {
                handleStepByStepFlow(query);
                return;
            }

            // Normal conversation handling
            if (query.includes("slider") || query.includes("panel") || query.includes("interactive")) {
                openSlidersForm();
            } else if (query.includes("step") || query.includes("chat") || query.includes("measure")) {
                startStepByStepFlow();
            } else if (query.includes("how") || query.includes("knn") || query.includes("model") || query.includes("accuracy")) {
                addBotMessage("I am programmed to analyze the physical measurements of a flower (sepal and petal dimensions) and identify its species instantly.");
                showWelcomeOptions();
            } else if (query.includes("catalog") || query.includes("species") || query.includes("flower") || query.includes("setosa") || query.includes("versicolor") || query.includes("virginica")) {
                explainSpecies();
            } else if (query.includes("hi") || query.includes("hello") || query.includes("hey")) {
                addBotMessage("Hi there! How can I help you identify Iris flowers today? Feel free to start a prediction!");
                showWelcomeOptions();
            } else {
                addBotMessage("I'm not sure how to answer that directly. Would you like to classify a flower using our interactive form or step-by-step chat?");
                showWelcomeOptions();
            }
        }

        // Reset conversation helper
        function resetChat() {
            const messagesContainer = document.getElementById("chatMessages");
            messagesContainer.innerHTML = "";
            currentConversationState = STATE_CHAT;
            flowMeasurements = { sl: null, sw: null, pl: null, pw: null };
            addBotMessage("Conversation reset! What would you like to do next?");
            showWelcomeOptions();
        }

        // Core KNN Engine implemented in JS
        function predictKNN(sl, sw, pl, pw, k = 5) {
            const distances = [];
            for (let i = 0; i < irisDataset.length; i++) {
                const point = irisDataset[i];
                // Euclidean distance calculation
                const dist = Math.sqrt(
                    Math.pow(point.sl - sl, 2) +
                    Math.pow(point.sw - sw, 2) +
                    Math.pow(point.pl - pl, 2) +
                    Math.pow(point.pw - pw, 2)
                );
                distances.push({ dist: dist, species: point.sp });
            }

            // Sort ascending by distance
            distances.sort((a, b) => a.dist - b.dist);

            // Fetch nearest K neighbors
            const neighbors = distances.slice(0, k);

            // Perform majority vote
            const votes = {};
            neighbors.forEach(n => {
                votes[n.species] = (votes[n.species] || 0) + 1;
            });

            let winner = "";
            let maxVotes = -1;
            for (const sp in votes) {
                if (votes[sp] > maxVotes) {
                    maxVotes = votes[sp];
                    winner = sp;
                }
            }

            return {
                species: winner,
                confidence: ((votes[winner] / k) * 100).toFixed(0),
                neighbors: neighbors
            };
        }

        // Display beautiful prediction card
        function displayPredictionResult(sl, sw, pl, pw) {
            showTypingIndicator();
            setTimeout(() => {
                removeTypingIndicator();
                const res = predictKNN(sl, sw, pl, pw);
                const info = speciesDetails[res.species];

                const cardHtml = `
                    <div class="result-card ${res.species}">
                        <div class="result-header">
                            <div>
                                <span class="result-species">${info.title}</span>
                                <div style="font-size: 11px; color: var(--text-muted); margin-top: 4px;">Predicted Species</div>
                            </div>
                            <div class="species-avatar">${info.emoji}</div>
                        </div>
                        <p class="result-desc">${info.desc}</p>
                        <div class="result-metrics">
                            <div class="metric-title">Input Dimensions & Reference Ranges</div>
                            <div class="metric-row">
                                <div class="metric-item">
                                    Sepal Length: <strong>${sl.toFixed(1)} cm</strong>
                                    <span style="font-size:10px; color: #6b7280;">Ref: ${info.sl}</span>
                                </div>
                                <div class="metric-item">
                                    Sepal Width: <strong>${sw.toFixed(1)} cm</strong>
                                    <span style="font-size:10px; color: #6b7280;">Ref: ${info.sw}</span>
                                </div>
                                <div class="metric-item">
                                    Petal Length: <strong>${pl.toFixed(1)} cm</strong>
                                    <span style="font-size:10px; color: #6b7280;">Ref: ${info.pl}</span>
                                </div>
                                <div class="metric-item">
                                    Petal Width: <strong>${pw.toFixed(1)} cm</strong>
                                    <span style="font-size:10px; color: #6b7280;">Ref: ${info.pw}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                `;

                const row = document.createElement("div");
                row.className = "message-row bot";
                row.innerHTML = cardHtml;
                
                const container = document.getElementById("chatMessages");
                container.appendChild(row);
                scrollToBottom();

                setTimeout(() => {
                    addBotMessage("Would you like to perform another prediction?");
                    showWelcomeOptions();
                }, 1000);
            }, 1200);
        }

        // Interactive Sliders Form Generator
        function openSlidersForm() {
            addBotMessage("Here is the visual classification panel. Adjust the sliders below to your flower's measurements and tap Predict!");
            
            const formId = "slider_form_" + Date.now();
            const formHtml = `
                <div class="slider-card" id="${formId}">
                    <div class="slider-title">
                        <span>🌸</span> Flower Dimension Panel
                    </div>
                    
                    <div class="slider-group">
                        <div class="slider-header">
                            <span class="slider-label">Sepal Length</span>
                            <span class="slider-value" id="val_sl">5.8 cm</span>
                        </div>
                        <input type="range" id="input_sl" min="4.0" max="8.0" step="0.1" value="5.8" oninput="updateSliderVal('sl', this.value)">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span class="slider-label">Sepal Width</span>
                            <span class="slider-value" id="val_sw">3.0 cm</span>
                        </div>
                        <input type="range" id="input_sw" min="2.0" max="4.5" step="0.1" value="3.0" oninput="updateSliderVal('sw', this.value)">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span class="slider-label">Petal Length</span>
                            <span class="slider-value" id="val_pl">4.3 cm</span>
                        </div>
                        <input type="range" id="input_pl" min="1.0" max="7.0" step="0.1" value="4.3" oninput="updateSliderVal('pl', this.value)">
                    </div>

                    <div class="slider-group">
                        <div class="slider-header">
                            <span class="slider-label">Petal Width</span>
                            <span class="slider-value" id="val_pw">1.3 cm</span>
                        </div>
                        <input type="range" id="input_pw" min="0.1" max="2.5" step="0.1" value="1.3" oninput="updateSliderVal('pw', this.value)">
                    </div>

                    <button class="predict-btn" onclick="submitSliders('${formId}')">
                        Predict Species 🌸
                    </button>
                </div>
            `;

            const row = document.createElement("div");
            row.className = "message-row bot";
            row.innerHTML = formHtml;
            document.getElementById("chatMessages").appendChild(row);
            scrollToBottom();
        }

        function updateSliderVal(param, val) {
            document.getElementById("val_" + param).innerText = val + " cm";
        }

        function submitSliders(formId) {
            const sl = parseFloat(document.querySelector(`#${formId} #input_sl`).value);
            const sw = parseFloat(document.querySelector(`#${formId} #input_sw`).value);
            const pl = parseFloat(document.querySelector(`#${formId} #input_pl`).value);
            const pw = parseFloat(document.querySelector(`#${formId} #input_pw`).value);

            // Disable button to prevent double-click
            const btn = document.querySelector(`#${formId} .predict-btn`);
            btn.disabled = true;
            btn.style.opacity = "0.7";
            btn.innerText = "Processing...";

            addUserMessage(`Sepal: ${sl}x${sw} cm, Petal: ${pl}x${pw} cm`);
            displayPredictionResult(sl, sw, pl, pw);
        }

        // Step-by-Step Chatbot Flow
        function startStepByStepFlow() {
            currentConversationState = STATE_ASK_SL;
            flowMeasurements = { sl: null, sw: null, pl: null, pw: null };
            addBotMessage("Alright, let's classify step-by-step! Please type or send the **Sepal Length** in cm (range: 4.0 - 8.0):");
        }

        function handleStepByStepFlow(query) {
            const val = parseFloat(query);
            if (isNaN(val)) {
                addBotMessage("Please enter a valid numerical number (e.g. 5.2):");
                return;
            }

            if (currentConversationState === STATE_ASK_SL) {
                if (val < 3.0 || val > 9.0) {
                    addBotMessage("That sepal length seems abnormal for an Iris (typically 4.0 - 8.0 cm). Please verify and enter again:");
                    return;
                }
                flowMeasurements.sl = val;
                currentConversationState = STATE_ASK_SW;
                addBotMessage(`Sepal Length set to **${val} cm**. Now, please enter the **Sepal Width** in cm (typically 2.0 - 4.5):`);
            } 
            else if (currentConversationState === STATE_ASK_SW) {
                if (val < 1.5 || val > 5.0) {
                    addBotMessage("That sepal width seems abnormal (typically 2.0 - 4.5 cm). Please enter again:");
                    return;
                }
                flowMeasurements.sw = val;
                currentConversationState = STATE_ASK_PL;
                addBotMessage(`Sepal Width set to **${val} cm**. Next, please enter the **Petal Length** in cm (typically 1.0 - 7.0):`);
            } 
            else if (currentConversationState === STATE_ASK_PL) {
                if (val < 0.5 || val > 8.0) {
                    addBotMessage("That petal length seems abnormal (typically 1.0 - 7.0 cm). Please enter again:");
                    return;
                }
                flowMeasurements.pl = val;
                currentConversationState = STATE_ASK_PW;
                addBotMessage(`Petal Length set to **${val} cm**. Finally, enter the **Petal Width** in cm (typically 0.1 - 2.5):`);
            } 
            else if (currentConversationState === STATE_ASK_PW) {
                if (val < 0.0 || val > 3.0) {
                    addBotMessage("That petal width seems abnormal (typically 0.1 - 2.5 cm). Please enter again:");
                    return;
                }
                flowMeasurements.pw = val;
                currentConversationState = STATE_CHAT; // Reset state back
                addBotMessage(`Perfect! All dimensions captured. Classifying...`);
                displayPredictionResult(flowMeasurements.sl, flowMeasurements.sw, flowMeasurements.pl, flowMeasurements.pw);
            }
        }

        // Informative sections
        function explainSpecies() {
            showTypingIndicator();
            setTimeout(() => {
                removeTypingIndicator();
                addBotMessage("🌸 **The Iris Dataset Species Catalog:**\\n\\n• **Iris Setosa**: Characterized by extremely short, narrow petals. Easiest to classify linearly due to distinct small size.\\n• **Iris Versicolor**: Mid-sized petals and sepals. Has slight dimensional overlap with Virginica.\\n• **Iris Virginica**: The largest and most robust flowers. High petal length and width values.");
                setTimeout(() => showWelcomeOptions(), 600);
            }, 800);
        }

        // Chat utilities
        function addBotMessage(text) {
            const formattedText = parseMarkdown(text);
            const bubble = document.createElement("div");
            bubble.className = "message-row bot";
            bubble.innerHTML = `<div class="message-bubble">${formattedText}</div>`;
            document.getElementById("chatMessages").appendChild(bubble);
            scrollToBottom();
        }

        function addUserMessage(text) {
            const bubble = document.createElement("div");
            bubble.className = "message-row user";
            bubble.innerHTML = `<div class="message-bubble">${text}</div>`;
            document.getElementById("chatMessages").appendChild(bubble);
            scrollToBottom();
        }

        function addBotOptions(options) {
            const container = document.createElement("div");
            container.className = "message-row bot";
            
            const chips = document.createElement("div");
            chips.className = "chips-container";
            
            options.forEach(opt => {
                const btn = document.createElement("button");
                btn.className = "chip-btn";
                btn.innerHTML = opt.text;
                btn.onclick = () => {
                    // Remove other options from click
                    chips.style.pointerEvents = "none";
                    chips.style.opacity = "0.6";
                    
                    addUserMessage(opt.text.replace(/^[^\s]+\s/, "")); // Strip emoji prefix for user message
                    
                    if (opt.action === "open_sliders") {
                        openSlidersForm();
                    } else if (opt.action === "start_chat_flow") {
                        startStepByStepFlow();
                    } else if (opt.action === "explain_species") {
                        explainSpecies();
                    }
                };
                chips.appendChild(btn);
            });
            
            container.appendChild(chips);
            document.getElementById("chatMessages").appendChild(container);
            scrollToBottom();
        }

        function showTypingIndicator() {
            const row = document.createElement("div");
            row.className = "message-row bot";
            row.id = "typingIndicator";
            row.innerHTML = `
                <div class="typing-indicator">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            `;
            document.getElementById("chatMessages").appendChild(row);
            scrollToBottom();
        }

        function removeTypingIndicator() {
            const indicator = document.getElementById("typingIndicator");
            if (indicator) {
                indicator.remove();
            }
        }

        function handleFormSubmit(e) {
            e.preventDefault();
            const input = document.getElementById("chatInput");
            const text = input.value.trim();
            if (!text) return;
            
            input.value = "";
            addUserMessage(text);
            
            showTypingIndicator();
            setTimeout(() => {
                removeTypingIndicator();
                handleUserMessage(text);
            }, 600);
        }

        function scrollToBottom() {
            const container = document.getElementById("chatMessages");
            container.scrollTop = container.scrollHeight;
        }

        // Micro-Markdown Parser
        function parseMarkdown(text) {
            return text
                .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\*(.*?)\\*/g, '<em>$1</em>')
                .replace(/\\n/g, '<br>');
        }
    </script>
</body>
</html>
"""

    # Do a simple string replacement to avoid f-string escaping headaches
    final_html = html_content.replace("{dataset_json}", dataset_json)

    # Write to C:\Users\karra\.gemini\antigravity\scratch\IA\data_classification\chatbot.html
    chatbot_path = "chatbot.html"
    with open(chatbot_path, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"Chatbot interface successfully generated at '{chatbot_path}'!")

if __name__ == "__main__":
    main()
