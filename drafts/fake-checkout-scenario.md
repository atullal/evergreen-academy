# Scenario: The Fake Checkout

**Goal:** A zero-risk sandbox where users practice checking the website address for tricks and choosing the safest payment method.

## UI Layout Instructions

*   **Screen Title:** "Practice Checkout" (Large, friendly font).
*   **Instruction Banner (Top):** "Welcome to the Practice Checkout! No real money is used here. Your goal is to check if this store is real, and if it is, pick the safest way to pay."
*   **The Browser Bar (Very prominent):** A gray bar at the top that looks like an internet address bar. It will display the website address in large, clear text so the user can inspect it.
*   **The Page Content:** A standard checkout screen showing a shopping cart summary (e.g., "1x Coffee Maker - $45.00").
*   **Payment Options (Radio buttons):**
    *   ( ) Credit Card
    *   ( ) Debit Card / Bank Transfer
    *   ( ) Target Gift Card
*   **Action Buttons (Bottom):**
    *   [ 🛒 Submit Payment ] (Green button)
    *   [ 🛑 Leave this Website ] (Red button)

## The Challenges

The simulator will show two checkout screens in a row.

### Challenge 1: The Sneaky Copycat
*   **Browser Bar URL:** `www.amaz0n-update-store.com`
*   **Correct Action:** User clicks [ 🛑 Leave this Website ].
*   **Incorrect Action:** User selects any payment method and clicks [ 🛒 Submit Payment ].

### Challenge 2: The Real Store
*   **Browser Bar URL:** `www.amazon.com`
*   **Correct Action:** User selects "Credit Card" and clicks [ 🛒 Submit Payment ].
*   **Incorrect Action 1:** User selects "Debit Card / Bank Transfer" or "Target Gift Card" and submits.
*   **Incorrect Action 2:** User clicks [ 🛑 Leave this Website ].

## Feedback Loops (The "Gentle Failure")

### Gentle Failure: Paying on a Fake Website
"Oops! That one was a sneaky trick. 

If you look closely at the address bar, it says **'amaz0n-update-store.com'** instead of the real **'amazon.com'**. In the real world, this copycat website would steal your payment information. But **here in the simulator, you are completely safe!** You did not break anything or lose any money.

Always check the top of the screen to make sure the store's name is spelled perfectly. Let's take a deep breath and try another one!"

### Gentle Failure: Choosing a Risky Payment Method
"You checked the website address, and it was the real store! Well done. 

However, you chose a payment method that does not protect you very well. A Debit Card takes money directly out of your actual bank account immediately. If a mistake happens, it is very hard to get that money back. (And remember, Gift Cards should never be used to pay for everyday online shopping).

**Credit Cards are the safest choice.** If a criminal steals a credit card number, they are spending the bank's money, not yours. The bank will usually cancel the fake charge for you. Let's try again!"

### Success Message
"Perfect! You did two very important things right:

1. You checked the website address and saw it was the real, perfectly spelled store.
2. You picked a Credit Card, which gives you the strongest protection if anything ever goes wrong.

You are becoming a very confident and safe online shopper. Great job!"