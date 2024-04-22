# What this is

This simple python programs converts WordPress posts to a format that Jekyll's feed system can understand.

I recovered my old blog posts from my old WordPress-Blog that way.

# Usage

1. Spin up a docker-container with a copy of your WordPress-database.

For me this ment recovering some old backups, mounting those into a mariadb-container, then creating a database-dump that could then be fed into a working mariadb-container.

The docker run command for future reference: (I already had a database-dump at `/tmp/wordpress-rescue/mariadb` )

```bash
docker run --name mariadb-wp -p 127.0.0.1:30306:3306 -v /tmp/wordpress-rescue/mariadb/:/docker-entrypoint-initdb.d -e MARIADB_ROOT_PASSWORD=supersicherespasswort -e MYSQL_ROOT_HOST=% -d mariadb:11
```

It will probably be easier if you already have a running database.

2. Create and launch the python-`venv` with `requirements.txt` (please just google for instructions)

3. Connect to a database (locally or not) by setting the `MARIADB_CONNSTR` to a valid connection string.

```bash
env MARIADB_CONNSTR='mariadb+mariadbconnector://USERNAME:PASSWORD@127.0.0.1:30306/wordpress' python3 wp-jekyll.py 
```
4. Voila! Your published blog posts will appear in a subdirectory called `output/`. (Need to create if doesn't exist)

Please alter this to suit your needs.
