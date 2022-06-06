# Dungeon Server
This is the back-end of [dungeon saga](https://github.com/ktei/dungeon-saga).

# Gettings started
- Install [Conda](https://docs.conda.io/projects/conda/en/latest/index.html)

- Install dependencies:
```
conda install --yes --file requirements.txt
```
- Run development server
```
sh ./scripts/dev.sh
```

NOTE that the default local port is 4000. You can change `dev.sh` to bind the server
to a different port.

# Conda commands
```
conda list -e > requirements.txt
conda install --yes --file requirements.txt
```
 
# What's next
- Dockerfile
- Production deployment configuration