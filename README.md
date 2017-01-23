# Compare-Two-Files
  
The idea behind this mini code project was to compare two files for discrepencies.  
  
Example:  
    File1 - contains names of servers from last week.  
    File2 - contains names of servers from this week.  


Tasks:  
You want to identify which servers from last week (File1) are still present in this week (File2).  
You want to identify which servers from last week (File1) no longer exist in this week (File2).  
And,  
You want to identify which servers from this week (File2) are new to the list that did not exist in last week (File1)   


Solution:  
  
To solve the above tasks you have to use Dictionaries (hashes).   
1. Read in File1 from last week, create a new hash and for each element create key == servername, value == 1  
2. Read in File2 from this week, create a new hash and for each element create key == servername, value == 1  
  
Now you have two hashes from last week and from this week.  
  
3. Now go through File1 hash and identify if each key from that hash exists in File2 hash.   
	If match is found then keep assigned value of 1 for that servername key  
	If no match is found then decrement value by 1 making it 0 for that servername key  
  
4. Now go through File2 hash and identify if each key from that hash exists in File1 hash   
	If match is found then keep assigned value of 1 for that servername key  
	If no match is found then increment value by 1 making it 2 for that servername key  
  
5. In the end you will be left with the following values for each key  
	0 = server from File1 no longer exists in File2 which could indicate it was down or has been decomissioned.  
	1 = server from File1 still exists in File2 which means no change occured.  
	2 = indicates new server has been added in File2 that never existed in File1, which could indicate a new build  
  


