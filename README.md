*Few utility scripts for day to day use.

1. battery test.sh
__________________
Lithium Ion battery usually has the longest lifespan if the charge in it maintained between 60 to 80 percent.
Keeping the battery charget at 100% all the time reduces the lifespan and so does draining it constantly.
Since I am in no mood to spend another 2K on the battery any time soon, this script constantly reminds me to plug or
unplug the charger in very kind words. Put it in cron with the desired frequency.
* TODO
______
Learn awk. No friggin clue how line number 2 works :/

2. conky.sh
___________
Launch conky at startup. Added this script to startup applications.

3. dictionary.py
________________
Tired of opening browser/dictionary every time I want to search a new word. :/
just select/copy the word U want to search and launch this script from a keyboard shortcut and it notifies you with meanings, examples.
Needs nltk library though, which is friggin huge! (around 700MB)
