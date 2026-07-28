# Scenario: The Phishing Inbox

**Goal:** Provide a safe, interactive environment for users to practice spotting scam emails without fear of real-world consequences.

## UI Layout Instructions

*   **Screen Title:** "Practice Inbox" (Large, clear font).
*   **Instruction Banner (Top):** "Welcome to your Practice Inbox! This is a safe space. No real money or personal information is connected here. Read the emails below and practice spotting the tricks. Click 'This is a Scam' or 'This is Safe' for each one."
*   **Layout:** A standard email view. A list of 4 emails on the left. When clicked, the email content appears on the right.
*   **Action Buttons (Bottom of each email):** 
    *   [ 🚨 This is a Scam ] (Red button)
    *   [ ✅ This is Safe ] (Green button)

## The Emails

### Email 1: The Urgent Invoice (Scam)
*   **Sender Name:** Billing Department
*   **Sender Address (Hidden details):** `billing-update-992@scam-example.com`
*   **Subject:** Receipt for your recent purchase - $499.99
*   **Body:** 
    Dear Customer, 
    Your credit card has been charged $499.99 for your annual computer support subscription. If you did not authorize this purchase, you must click the link below immediately to cancel the charge and get a refund.
    [Link: Cancel Charge Now]
*   **Flags:** Urgency ("immediately"), Money ($499.99).

### Email 2: The Fake Grandchild (Scam)
*   **Sender Name:** Emergency
*   **Sender Address (Hidden details):** `helpme-221@random-mail.com`
*   **Subject:** Please help, I'm in trouble!
*   **Body:**
    Hi, it's me. I lost my phone and I am stranded. Please don't tell mom and dad, they will be so mad at me. I need you to buy $200 in Apple gift cards and send me the codes so I can get a ride home. Please hurry!
    [Link: How to buy gift cards]
*   **Flags:** Urgency ("hurry"), Secrecy ("don't tell mom"), Money (Gift cards).

### Email 3: The Account Lock (Scam)
*   **Sender Name:** Bank Security
*   **Sender Address (Hidden details):** `security-alert@not-a-real-bank.com`
*   **Subject:** URGENT: Your account will be locked
*   **Body:**
    We noticed unusual activity on your account. For your safety, we will permanently lock your account in 12 hours unless you verify your identity. Click the link below to log in and confirm your password.
    [Link: Verify Password Now]
*   **Flags:** Urgency ("12 hours", "permanently lock").

### Email 4: The Real Email (Safe)
*   **Sender Name:** Martha
*   **Sender Address:** `martha.friend@email.com`
*   **Subject:** Sunday dinner recipe
*   **Body:**
    Hi! I was hoping you could send me that wonderful chicken recipe you made last week? No rush at all, just whenever you have a moment. Hope you are doing well! 
    Love, Martha.
*   **Flags:** None. No links, no urgency, known sender context.

## Feedback Loops (The "Gentle Failure")

When the user clicks the wrong button (e.g., clicks the link inside a scam email, or marks a scam as 'Safe'), a friendly pop-up appears.

### Gentle Failure Message (for clicking a Scam)
"Oops! That one was a trick. 

In the real world, clicking that link could be dangerous, but **here in the simulator, you are completely safe!** You did not break anything.

Remember our golden rule: this email tried to make you panic by using **Urgency** and asking for **Money**. 

Next time you see a message like this, close the email. If you are worried, call the person or the company directly using a phone number you already know and trust. Let's take a deep breath and try the next one!"

### Success Message
"Great job! You spotted the trick. 

By slowing down and noticing the warning signs (like urgency or asking for money), you kept your information safe. You are doing wonderfully. Let's keep going!"