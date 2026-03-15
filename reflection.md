# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
1. Go higher/lower hints are swapped: When "Show hint" is checked and I guess a number that is too low, a "Go LOWER!" hint is given. When I guess a number that is too high, a "Go HIGHER!" hint is given. However, I expected the "Go LOWER!" hint to be given when my number is too high and the "Go HIGHER!" hint to be given when my number is too low.
2. "New Game" button does nothing: When I click the "New Game" button, nothing happens. However, I expected this to start a new game (reset existing guess history, attempts, and score, and change secret number).
3. Out of bound inputs are allowed: When I input a number which is outside the given range of numbers, (such as a number less than 1 or greater than 100), the number still goes through and I do not get informed that my number is out of bounds. However, I expected to be notified if my number is out of bounds and not have that number count towards my allotted guess attempts.

---

## 2. How did you use AI as a teammate?
I used Copilot on this project. One AI suggestion that was correct is its suggestion to swap "Go Higher" and "Go Lower" messages to fix the bug that those messages were reversed in the Streamlit UI. I verified that this fix by asking Copilot to generate relevant pytest cases and I also tested new behavior myself using high and low guesses in the Streamlit UI. However, when I asked Copilot to generate pytest test cases to test that "Go Higher" and "Go Lower" messages were displayed appropriately, Copilot did add two new test cases but did not delete existing test cases which incorrectly tested the same behavior.  I verified the result by seeing that the incorrect test cases had failed, and asked Copilot to delete those cases.

---

## 3. Debugging and testing your fixes
I decided whether a bug was really fixed by first writing a test case to test that the new feature works as expected. I then re-ran the Streamlit program and tested the feature out myself to make sure that it still works as expected. One test I ran using pytest was to test that the "New Game" button resets the game state. This test showed me that my code had to be designed such that resetting game state was separate from Streamlit commands, to ensure testability. AI designed all my tests, but before accepting its test cases, I always verified that each one was written correctly and that it tests exactly what it needed to test. I also verified that there were no redundant test cases (which happened once).

---

## 4. What did you learn about Streamlit and state?
Streamlit runs the entire program again every time the user interacts with the program (such as entering input). This is known as a "rerun". Because of this, Streamlit needs a way to preserve existing game state values. To keep track of game state between the reruns (such as attempts remaining), Streamlit stores those game state values in a session state (program's memory).

---

## 5. Looking ahead: your developer habits
One strategy I want to reuse in future projects is incremental testing. Testing a feature right after I implemented it ensured that I was on stable ground before continuing on with my project and allowed me to fix any uncaught bugs before moving on with the project. Something I would do differently with AI is to make my prompts really specific. I noticed that when my promtps were not super specific to what I wanted the AI to do, it would do more than I wanted it to do (for example it offered to install packages in VSCode). Prior to doing this project, I assumed that using AI-generated code in projects would be really easy to do, but going through this project taught me that using AI generated code is not as easy as it seems and that there has to be a human supervising all changes the AI offers to make.

