# Synchronize Update from the Starter Pack

The teacher team will sometimes update the base repository with new update

# From the Terminal

Open the terminal in VScode ($ctrl+j$) then type the following command

## Add the starterPack as a Remote (to do-once)

It is not necessary to create a local branch, but i

```bash
# Add the startpack as a remote
git remote add starterPack https://github.com/Estia-advanced-programming/pandora-starterpack.git
git fetch starterPack --prune
```

Optionally you can have a local branch to see the change locally.

```bash
# Create a local branch that track the main 
git checkout -B temp
git checkout -B starterPack-main --track starterPack/main
git 
git checkout -
```

## Merge Updates from Starterpack

```bash
git fetch starterPack --prune
git merge starterPack/main -X theirs
```
