# Cole goes for gold

I'm really going for the full thing this year. I am writing a journal to go along with my progress and I will add to it here.

## Day 1

### Part 1

Task: Get the distances between each of the elements from the list after being sorted and sum these distances

```plaintext
3   4
4   3
2   5
1   3
3   9
3   3
```

### Part 2

This is a slightly more fun idea. Instead of an i to i comparison, now we have to calculate the sum of the count(i) from the right list for i in the left list

## Day 2

I'm writing this from day 3. The first part was easy enough with a simple "assume the condition is true and then prove it false" approach for each line, but then it really threw a curveball with Part 2! Thinking about how to intelligently do a single scan for each line that considers removing elements was quite a brain teaser. Feels like a Leetcode medium honestly. So I left it to work on in Day 3 and went to bed. I did just decide to brute force it by trying to remove each element and see if one works. But the solution with this "trade simplicity for time" tradeoff is so clean I like it just as well. Honestly, it just makes me grateful I don't have to be on the Leetcode grind now.

## Day 3

**Regex time!!!** I could smell it as soon as I saw the problem. I do love a good regex and playing with them in an online playground like [Regexr](https://regexr.com/) is really enjoyable. I used the sample input to make my Regex and then ported it into Python and added some simple logic and boom! Part 1 was finished! Then Part 2 added some fun complexity, almost turning the thing into a Turing machine style problem. Weird tangle with non-capturing vs capturing groups had me resort to ChatGPT, and the solution was so simple it made me regret asking it instead of RTFM. But hey it was still fun! Excited to be still feeling comfortable at this stage, but very nervous going forward.

- **Part 1 regex:** `mul\([1-9]+[0-9]*,[1-9]+[0-9]*\)`
- **Part 2 regex:** `(?:mul\([1-9][0-9]*,[1-9][0-9]*\)|do\(\)|don't\(\))`
