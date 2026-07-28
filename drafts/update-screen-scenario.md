# Scenario: The Update Screen

**Goal:** A zero-risk sandbox where users practice telling the difference between a real, safe device update and a fake, scary internet pop-up that tries to trick them.

## UI Layout Instructions

*   **Screen Title:** "Practice Updates" (Large, friendly font).
*   **Instruction Banner (Top):** "Keeping your device updated is important for safety, but scammers often fake update screens. Look at the screens below. Decide if it is a real system update or a fake internet trick. You cannot break anything here!"
*   **Action Buttons (Bottom):**
    *   [ ⚙️ Install Update ] (Blue button)
    *   [ 🛑 Close and Ignore ] (Red button)

## The Challenges

The simulator will show two different screens, one after the other.

### Challenge 1: The Fake Pop-Up (Scam)
*   **Visual Frame:** A web browser window with an address bar at the top (e.g., `www.free-news-website.com`).
*   **The Content:** A loud, brightly colored box right in the middle of the screen.
*   **Text:** "⚠️ WARNING! Your phone has a virus! It is severely damaged! You MUST click here to install an urgent update right now or lose all your photos!" (Flashing red and yellow colors).
*   **Correct Action:** User clicks [ 🛑 Close and Ignore ].
*   **Incorrect Action:** User clicks [ ⚙️ Install Update ].
*   **Flags:** Urgency ("right now", "MUST"), inside a web browser, uses fear and threats.

### Challenge 2: The Real Settings Menu (Safe)
*   **Visual Frame:** A calm, clean screen that looks like the "Settings" app on a phone (no web browser address bar).
*   **The Content:** Simple, plain text on a white or gray background.
*   **Text:** "Software Update. A new update is available for your device. This update includes bug fixes and security improvements. It will take about 10 minutes to complete."
*   **Correct Action:** User clicks [ ⚙️ Install Update ].
*   **Incorrect Action:** User clicks [ 🛑 Close and Ignore ].
*   **Flags:** Calm tone, no urgency, no threats, located in the device settings.

## Feedback Loops (The "Gentle Failure")

### Gentle Failure: Clicking the Fake Pop-Up
"Oops! That one was a sneaky trick. 

In the real world, clicking that warning might download a bad program. But **here in the simulator, you are completely safe!** 

Remember our Golden Rule: scammers try to make you panic. Real device updates never yell at you, flash red, or say you have a virus. They are quiet and polite. If a screen is trying to scare you into acting quickly, it is always a trick. Let's take a deep breath and try the next one!"

### Gentle Failure: Ignoring the Real Update
"You chose to ignore the update. It is always good to be cautious! 

However, this one was a real, safe update. Notice how the screen was calm, polite, and didn't try to scare you? Real updates live in your device's 'Settings' app, not on websites. 

Keeping your device updated is like locking your front door—it is the best way to keep the bad guys out. When you see a calm, polite update in your settings, it is safe to install it. Let's try again!"

### Success Message
"Excellent work! 

You saw right through the scary fake pop-up and closed it. You also recognized the quiet, polite tone of a real system update and installed it to keep your device safe. 

Remember: if a screen tries to scare you or rush you, it's a trick. Real updates are calm and helpful. You are doing a wonderful job!"