import datetime

TOPICS = [
    "How to clean a coffee maker",
    "What is cloud storage",
    "How often to replace air filters",
    "What does Bluetooth do",
    "How to organize email inbox"
]

def generate_article(topic):
    today = datetime.date.today()
    return f"""---
title: {topic}
date: {today}
description: Educational guide about {topic.lower()}.
---

## {topic}

This article provides general, informational content for educational purposes only.

### Overview
{topic} is a commonly searched topic. This guide explains it in simple terms.

### Key Points
- General explanation
- Common use cases
- Basic tips

### Disclaimer
This content is informational only and does not constitute professional advice.
"""

def main():
    topic = TOPICS[today().day % len(TOPICS)]
    article = generate_article(topic)
    filename = f"content/articles/{topic.replace(' ', '_').lower()}.md"
    with open(filename, "w") as f:
        f.write(article)

if __name__ == "__main__":
    main()
