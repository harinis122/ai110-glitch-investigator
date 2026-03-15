# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
1. Go higher/lower hints are swapped: When "Show hint" is checked and I guess a number that is too low, a "Go LOWER!" hint is given. When I guess a number that is too high, a "Go HIGHER!" hint is given. However, I expected the "Go LOWER!" hint to be given when my number is too high and the "Go HIGHER!" hint to be given when my number is too low.
2. "New Game" button does nothing: When I click the "New Game" button, nothing happens. However, I expected this to start a new game (reset existing guess history, attempts, and score, and change secret number).
3. Out of bound inputs are allowed: When I input a number which is outside the given range of numbers, (such as a number less than 1 or greater than 100), the number still goes through and I do not get informed that my number is out of bounds. However, I expected to be notified if my number is out of bounds and not have that number count towards my allotted guess attempts.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot on this project. One AI suggestion that was correct is its suggestion to swap "Go Higher" and "Go Lower" messages to fix the bug that those messages were reversed in the Streamlit UI. I verified that this fix by asking Copilot to generate relevant pytest cases and I also tested new behavior myself using high and low guesses in the Streamlit UI.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?





---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
