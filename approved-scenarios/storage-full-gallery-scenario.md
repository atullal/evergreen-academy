# Scenario: The "Storage Full" Gallery

**Goal:** A zero-risk sandbox where users practice making space on their device by deleting unwanted photos, while learning that mistakes can be undone via the "Recently Deleted" folder.

## UI Layout Instructions

*   **Screen Title:** "Practice Photo Gallery" (Large, friendly font).
*   **Instruction Banner (Top):** "Your device storage is full! Let's make some space. Look at the photos below. Tap the ones that are blurry or mistakes, and tap 'Delete'. Don't worry—you cannot lose real photos here!"
*   **Layout:** A grid of 6 photographs, like a smartphone photo album.
*   **Action Buttons (Bottom):**
    *   [ 🗑️ Delete Selected Photos ] (Red button)
    *   [ ↩️ Undo (Recently Deleted) ] (Blue button)

## The Photos

The gallery displays a mix of photos to test decision-making:

1.  **Photo 1 (Keeper):** A clear, smiling photo of a family at a birthday party.
2.  **Photo 2 (Junk - Blurry):** A completely blurry, unrecognizable smear of colors (someone moved the camera too fast).
3.  **Photo 3 (Junk - Accidental):** A dark, blurry photo of the inside of a pocket or a foot.
4.  **Photo 4 (Keeper):** A nice, clear picture of a pet dog sitting still.
5.  **Photo 5 (Junk - Duplicate):** A picture of a garden flower (looks exactly like Photo 6).
6.  **Photo 6 (Keeper - Best shot):** A picture of the exact same garden flower, but slightly brighter and better framed.

**Correct Action:** User selects Photos 2, 3, and 5, then clicks [ 🗑️ Delete Selected Photos ].
**Incorrect Action 1:** User selects a "Keeper" (Photo 1, 4, or 6) and clicks Delete.
**Incorrect Action 2:** User clicks Delete without selecting enough junk photos.

## Feedback Loops (The "Gentle Failure")

### Gentle Failure: Deleting a "Keeper" (Showing the Safety Net)
"Oops! You deleted a nice, clear family photo. 

In real life, deleting a precious memory can feel scary. But **here in the simulator, nothing is permanently lost!** 

Even on your real phone, when you delete a photo, it doesn't vanish immediately. It goes to a safe place called the **'Recently Deleted'** folder for about a month. If you make a mistake, you can always go into that folder and put the picture back. 

Try clicking the blue [ ↩️ Undo (Recently Deleted) ] button to bring the photo back, and then try selecting only the blurry ones."

### Gentle Failure: Not Deleting Enough
"You are being very careful, which is great! 

However, your storage is still a bit too full. To make room for new memories, we need to let go of the accidents. Try to find the photo that is completely blurry, the picture of the foot, and the extra picture of the flower. 

Remember, it's safe to practice here. Let's try again!"

### Success Message
"Wonderful job! 

You successfully cleared out the blurry mistakes and duplicates, leaving plenty of room for new, beautiful memories. 

Remember: managing your storage is like cleaning out a real closet. It's a normal part of owning a device, and the 'Recently Deleted' folder is always there to catch any accidental mistakes. You did great!"

---
**Approval:**
- **Reviewer:** Quill
- **Date:** 2026-07-28
- **Checklist Version:** v2-simulator
