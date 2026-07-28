# Scenario: The App Permissions Prompt

**Goal:** A zero-risk sandbox where users practice thinking critically about what personal information an app actually needs to do its job, and learn that it is perfectly okay to say "No".

## UI Layout Instructions

*   **Screen Title:** "Practice App Install" (Large, friendly font).
*   **Instruction Banner (Top):** "When you open a new app, it might ask for permission to see your personal information. You are in charge—you get to say yes or no! Let's practice with a new Flashlight app. You cannot break anything here!"
*   **Visual Frame:** A screen showing a simple app called "Super Bright Flashlight" opening for the first time.
*   **The Pop-up:** A small box in the middle of the screen asking a question.
*   **Action Buttons (Inside the pop-up):**
    *   [ ❌ Deny (Say No) ] (Red text or button)
    *   [ ✅ Allow (Say Yes) ] (Blue text or button)

## The Challenges

The simulator will show three pop-up questions in a row for the "Super Bright Flashlight" app.

### Challenge 1: The Contacts List
*   **Pop-up Text:** "Super Bright Flashlight would like to access your Contacts."
*   **Correct Action:** User clicks [ ❌ Deny (Say No) ].
*   **Incorrect Action:** User clicks [ ✅ Allow (Say Yes) ].
*   **Context:** A flashlight has no reason to know the phone numbers of your friends and family.

### Challenge 2: The Microphone
*   **Pop-up Text:** "Super Bright Flashlight would like to access your Microphone."
*   **Correct Action:** User clicks [ ❌ Deny (Say No) ].
*   **Incorrect Action:** User clicks [ ✅ Allow (Say Yes) ].
*   **Context:** A flashlight does not need to listen to your conversations.

### Challenge 3: The Camera
*   **Pop-up Text:** "Super Bright Flashlight would like to access your Camera."
*   **Correct Action:** User clicks [ ✅ Allow (Say Yes) ].
*   **Incorrect Action:** User clicks [ ❌ Deny (Say No) ].
*   **Context:** The bright light on a phone is physically built into the camera. The app needs camera permission just to turn the light bulb on!

## Feedback Loops (The "Gentle Failure")

### Gentle Failure: Allowing Contacts or Microphone
"Oops! You clicked 'Allow' for that one. 

In the real world, an app could use that to read your address book or listen to you. But **here in the simulator, your privacy is completely safe!** 

When an app asks for permission, ask yourself: 'Does this app really need this to do its job?' A flashlight app only makes light. It does not need to call your friends, and it does not need to hear your voice. It is always safest to click 'Deny' if it doesn't make sense. Let's try the next one!"

### Gentle Failure: Denying the Camera
"You chose 'Deny'. It is always a great instinct to protect your privacy! 

However, this one is a little tricky. On most phones, the flashlight bulb is physically connected to the camera. So, a flashlight app *does* need permission to use the camera, just so it can turn the bulb on! 

If you accidentally deny something an app actually needs, the app simply won't work, and you can always change it later in your Settings. You didn't break anything. Let's try again!"

### Success Message
"Fantastic job! 

You thought carefully about exactly what the app needed. You protected your friends' phone numbers and your microphone, but you correctly allowed the camera so the light bulb could work. 

Remember: you are the boss of your device. If a permission doesn't make sense to you, always click 'Deny'. You are doing wonderfully!"