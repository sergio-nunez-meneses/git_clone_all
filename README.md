# Git clone all

Clone all public repositories from an user. To run the script, paste the following line in the terminal:

```
python3 git_clone_all.py
```

Then, you'll be ask to enter an Github username:

```
Github username:
```

Finally, a typical git clone response should be displayed:

```
Cloning into 'repository-1'...
remote: Enumerating objects: 44, done.
remote: Counting objects: 100% (44/44), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 44 (delta 10), reused 42 (delta 8), pack-reused 0
Unpacking objects: 100% (44/44), 8.08 KiB | 435.00 KiB/s, done.
Cloning into 'repository-2'...
remote: Enumerating objects: 52, done.
remote: Counting objects: 100% (52/52), done.
remote: Compressing objects: 100% (35/35), done.
remote: Total 734 (delta 16), reused 38 (delta 16), pack-reused 682
Receiving objects: 100% (734/734), 379.68 KiB | 411.00 KiB/s, done.
Resolving deltas: 100% (416/416), done.
Cloning into 'repository-3'...
```

A new folder, ```github```, should have be created at the script level with all the cloned repositories inside.

And that's it.
