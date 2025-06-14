# Simplified User Interface

This directory contains a simplified web user interface to interact with the Pyragogy co-authoring workflow without the need to manually build JSON payloads.

## Files

* `simple-input-interface.html` – A complete web interface to submit new ideas to the workflow

## How to Use

1. Ensure that n8n is running (see main README)
2. Open `simple-input-interface.html` in a web browser
3. Fill out the form with:

   * **Chapter Title**: A descriptive title for the new content
   * **Content/Initial Idea**: Raw text, ideas, or key points to be developed
   * **Tags**: Keywords to categorize the content
   * **Phase**: The state of the content (draft, review, final)
   * **Cognitive Rhythm**: The processing frequency
   * **Human Review**: Whether to require human approval
4. Click "Submit to AI Workflow"

## Features

* ✨ Modern and responsive interface
* 🏷️ Dynamic tag management
* 🔄 Real-time feedback on submission status
* 📱 Mobile-compatible
* 🎨 Intuitive and user-friendly design

## Configuration

The interface is preconfigured to connect to `http://localhost:5678/webhook/pyragogy/process`. If your n8n instance runs on a different URL, modify the "n8n Webhook URL" field in the interface.

## Example of Generated Payload

```json
{
  "title": "Introduction to Multi-Agent Orchestration",
  "input": "Description of orchestration techniques...",
  "tags": ["AI", "automation", "n8n"],
  "phase": "draft",
  "rhythm": "on-demand",
  "requireHitl": true
}
```
