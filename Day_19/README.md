# Problem Summary 🤖  
My solution to this problem is a pretty straightforward depth-first search of move options to generate the most geodes.  
The only special part in this solution is that I pruned the search using the following conditions:  
1. If the number of bots has reached the maximum amount of material needed for a new bot, then stop adding bots for the material.
2. If all of the current materials are more than the maximum amount required, then you must add a bot.  
3. If you can add a geode bot, do it.
4. Keep track of the materials for each configuration of bots. If you have the same number of bots with fewer materials, cut off the search.
  
These conditions keep the search at a reasonable time, although it still takes about a minute to get an answer.
