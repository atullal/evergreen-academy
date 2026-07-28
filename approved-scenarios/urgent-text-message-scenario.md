# Scenario: The Urgent Text Message

**Goal:** A zero-risk sandbox where users practice identifying scam text messages using the Golden Rule (Urgency + Secrecy + Money = Stop) and safely deleting them.

## UI Layout Instructions

*   **Screen Title:** "Practice Text Messages" (Large, friendly font).
*   **Instruction Banner (Top):** "Welcome to your Practice Phone! Read the text messages below. If it looks like a scam, delete it. If it looks like a normal message, you can reply. You cannot break anything here!"
*   **Layout:** A screen that looks like a smartphone text message app. The message appears in a speech bubble in the center of the screen. The sender's phone number is at the top.
*   **Action Buttons (Bottom):** 
    *   [ 💬 Reply ] (Blue button)
    *   [ 🗑️ Delete & Ignore ] (Red button)

## The Messages

The simulator will show three text messages, one after the other.

### Message 1: The Package Delivery (Scam)
*   **Sender:** `Unknown Number (555-0199)`
*   **Message Bubble:** "POSTAL SERVICE: Your package is on hold because of a missing $1.50 delivery fee. Click here to pay immediately or your package will be destroyed."
*   **Correct Action:** User clicks [ 🗑️ Delete & Ignore ].
*   **Incorrect Action:** User clicks [ 💬 Reply ].
*   **Flags:** Urgency ("immediately", "destroyed"), Money ($1.50).

### Message 2: The Grandchild in Trouble (Scam)
*   **Sender:** `Unknown Number (555-0244)`
*   **Message Bubble:** "Hi, it's me. I got into a small accident and the police have me. Please don't tell mom and dad. I need $500 for bail in gift cards. Reply quickly please!"
*   **Correct Action:** User clicks [ 🗑️ Delete & Ignore ].
*   **Incorrect Action:** User clicks [ 💬 Reply ].
*   **Flags:** Urgency ("quickly"), Secrecy ("don't tell mom and dad"), Money ($500 in gift cards).

### Message 3: The Doctor's Office (Safe)
*   **Sender:** `Dr. Smith's Office (555-0800)`
*   **Message Bubble:** "Reminder: You have an appointment with Dr. Smith tomorrow at 10:00 AM. Reply YES to confirm or NO to cancel."
*   **Correct Action:** User clicks [ 💬 Reply ].
*   **Incorrect Action:** User clicks [ 🗑️ Delete & Ignore ].
*   **Flags:** None. It is a standard appointment reminder.

## Feedback Loops (The "Gentle Failure")

### Gentle Failure: Replying to a Scam
"Oops! That text message was a trick. 

In the real world, replying to that message or clicking its link could cause trouble. But **here in the simulator, you are completely safe!** You did not break anything or lose any money.

Remember our Golden Rule: scammers try to make you panic. That message used **Urgency** and asked for **Money** (or to keep a **Secret**). Whenever you see those signs, the safest choice is to delete the message. If you are worried it might be real, ask a trusted family member for help. Let's take a deep breath and try the next one!"

### Gentle Failure: Deleting a Safe Message
"You chose to delete that message. That is always the safest choice if you are unsure! 

However, that one was actually a normal, safe reminder from a doctor's office. Notice how it didn't ask for money, didn't ask you to keep a secret, and didn't try to make you panic. It is perfectly safe to reply to messages like that. Let's try another one!"

### Success Message
"Great job! 

You remembered the Golden Rule perfectly. By recognizing the signs of Urgency, Secrecy, and Money, you knew exactly which messages were tricks and safely deleted them. You are doing a wonderful job protecting yourself. Let's keep going!"

---
**Approval:**
- **Reviewer:** Quill
- **Date:** 2026-07-28
- **Checklist Version:** v2-simulator
