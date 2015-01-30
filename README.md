# streamingstars

Modules to extend the [BLAST](http://rapidlasso.com/blast/) extension of [LAStools](http://rapidlasso.com/blast/) to construct a TIN and store it in postgreSQL.


## A star-based postgis table

```
createdb mytestdb
psql -d mytestdb -c "CREATE EXTENSION postgis;"
CREATE TABLE points (id  int, x  double precision, y  double precision, z  double precision, star integer[]);
```

```
mkfifo --mode=0666 stars.txt [creation of a named pipe]

COPY points from '/home/hugo/data/las/msh/stars.txt';

spfinalize -i input.las -level 6 -ospb | spdelaunay2d -ispb -osmb | python smb2star.py > stars.txt
```


## Triangles stored as Simple Feature POLYGONS

```
create table trianglesf();
SELECT AddGeometryColumn('public', 'trianglesf', 'geom', -1, 'POLYGON', 2);
spfinalize -i input.las -level 6 -ospb | spdelaunay2d -ispb -osmb | python smb2sf.py > stars.txt
copy trianglesf from '/home/hugo/data/las/msh/stars.txt';
create index trianglesf_gist on trianglesf using gist (geom);
