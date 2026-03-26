---
name: church-advertising
description: "Creates church advertising and social media content that matches the Reformed Baptist voice. Integrates with Facebook MCP for page management. Uses the orchestra for multi-model content refinement."
version: 1.0.0
---

# Church Advertising — Social Media Content

> *"How beautiful are the feet of those who preach the good news!"* — Romans 10:15

## Purpose

Creates social media content for the church's Facebook page that is:
- Theologically sound (Reformed Baptist)
- Voice-consistent (matches the preacher's established voice)
- Engaging without being promotional or manipulative
- Faithful to the church's mission and ethos

## Setup: Facebook MCP Server

### Install

```bash
# Option 1: HagaiHen's facebook-mcp-server (recommended)
claude mcp add facebook-server -- npx @hagaihen/facebook-mcp-server

# Option 2: BuilderHub's mcp-facebook
claude mcp add facebook -- npx mcp-facebook
```

### Configure

Create or add to your `.env`:
```
FACEBOOK_PAGE_ACCESS_TOKEN=<your-page-access-token>
FACEBOOK_PAGE_ID=<your-page-id>
```

### Get Facebook Credentials
1. Go to https://developers.facebook.com
2. Create an App (type: Business)
3. Add Facebook Login and Pages API products
4. Generate a Page Access Token with permissions:
   - `pages_read_engagement` — read posts and engagement data
   - `pages_manage_posts` — create and schedule posts
   - `pages_read_user_content` — read comments
5. Get your Page ID from Facebook Page → About → Page ID

### Verify
```bash
claude mcp list  # Should show facebook-server as Connected
```

## When to Fire

- On `/advertise` or `/social` command
- When discussing church social media, outreach, or advertising
- When preparing sermon announcements or event promotions

## Content Types

### 1. Sermon Announcement
Promote an upcoming sermon or series. Reference sermon-planner for what's being preached.

```
Voice: Invitational, not salesy. "Come hear..." not "Don't miss..."
Length: 2-3 sentences + Scripture reference
Image: Text overlay on simple background (no stock photos)
```

### 2. Sermon Reflection
Post-sermon content that gives people a taste of what was preached.

```
Voice: Reflective, draws from congregation-pulse observations
Length: Key quote from sermon + 1 sentence of context
Source: Pull from the actual sermon manuscript in this repo
```

### 3. Theological Encouragement
Standalone posts with theological depth appropriate for social media.

```
Voice: Steady, warm, doctrinally precise — like-a-human standards apply
Length: 1-3 sentences. The shorter the better.
Standard: Could a member share this and feel proud? Would a visitor feel welcomed?
```

### 4. Event Announcement
Church events, fellowship meals, special services.

```
Voice: Warm, specific (date/time/place), invitational
Length: Who, what, when, where. One sentence of warmth.
```

## Voice Guard

ALL social media content goes through the same voice standards as sermons:

- **like-a-human** — no AI-speak, no corporate filler, no promotional drift
- **voice-audit** — scan for machine tells before posting
- **careful-not-clever** — verify Scripture references, don't fabricate quotes

### What the Church Voice Is

- Direct, warm, theologically precise
- "Come and hear" not "Join us for an amazing experience"
- Scripture-first, not feeling-first
- The pastor's voice, not a marketing department's voice

### What the Church Voice Is NOT

- Promotional: "Best sermon series ever!"
- Manipulative: "You don't want to miss this!"
- Generic: "Join us this Sunday for worship" (every church says this)
- AI-generated: "In today's fast-paced world, finding peace can be challenging..."

### The Test

Before posting, ask:
1. Does this sound like the pastor wrote it on his phone?
2. Would a member recognize the voice?
3. Does the theology hold under scrutiny?
4. Is there a Scripture reference grounding the claim?

## Using the Orchestra

For important campaigns or series announcements, run the full orchestra:

```bash
cd /home/user/ken/orchestrator && python3 orchestra.py sermon "Create a Facebook post announcing our new sermon series on Romans 8 — theme: no condemnation, freedom in Christ, the Spirit's work"
```

Claude proposes content → GPT refines structure → Gemini expands reach → Grok challenges authenticity. Claude synthesizes the final post with verdicts on each model's input.

## Facebook Operations

### Read Recent Posts
```
"Show me our last 5 Facebook posts and their engagement"
```
Uses Facebook MCP to pull posts, likes, comments, shares.

### Analyze Engagement
```
"Which posts got the most engagement this month?"
```
Identifies what content resonates with the congregation online.

### Create a Post
```
"Draft a Facebook post for this Sunday's sermon on Romans 8:1"
```
Claude drafts → voice-audit → your approval → publish via MCP.

### Schedule a Post
```
"Schedule a sermon announcement for Saturday at 6 PM"
```
Creates the post and schedules it for optimal timing.

## Integration

- **sermon-planner** — what's being preached determines what's advertised
- **congregation-pulse** — what landed in the sermon informs the reflection post
- **sermon-map** — find the right sermon manuscript to quote from
- **like-a-human** — voice guard during content creation
- **voice-audit** — post-draft quality check
- **cognitive-memory** — remember what content worked, encode engagement patterns
- **orchestra** — multi-model refinement for important campaigns

## Content Calendar Pattern

| Day | Content Type | Source |
|-----|-------------|--------|
| Saturday | Sermon announcement | sermon-planner + this week's passage |
| Sunday PM | Sermon reflection | congregation-pulse + key quote |
| Wednesday | Theological encouragement | standalone, doctrinally rich |
| As needed | Event announcements | church calendar |

---

*Soli Deo Gloria* — Advertise faithfully. The gospel doesn't need hype. It needs heralds.
