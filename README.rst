==============
python-sqloose
==============

**Note: This is a pre-release version. I'm taking more time to decide if I want to change the
interface**

sqloose is a SQL-like query language that maps directly to SQL. This module does not implement a
database itself, but is instead a translator from sqloose to SQL.

Installation
------------

When no longer a pre-release, run:

pip install python-sqloose

Usage
-----

.. code-block:: python

    from sqloose import sqloose

    sql = sqloose.to_sql("SELECT age, race, gender, count(*) AS num FROM stats GROUP BY [1:3] ORDER BY -1 DESC")

Use Case
--------

sqloose is designed as a less rigid SQL, offering a more convenient syntax. In particular, it
allows ranges and negative indices to be used in GROUP BY and ORDER BY statements. The right index
in the range specifies the final item, unlike Python in which the right index is the final item +
1.

Take the following SQL statement:

.. code-block:: sql

    SELECT age, race, gender, count(*) AS num FROM stats GROUP BY 1,2,3 ORDER BY 4 DESC

In sqloose this can be represented many ways, such as:

.. code-block:: sql

    SELECT age, race, gender, count(*) AS num FROM stats GROUP BY [1:3] ORDER BY -1 DESC
    SELECT age, race, gender, count(*) AS num FROM stats GROUP BY [:3] ORDER BY -1 DESC
    SELECT age, race, gender, count(*) AS num FROM stats GROUP BY [:-2] ORDER BY -1 DESC

Further, sqloose defines the GROUP TO and GROUP THROUGH constructs, which can be used in the same
scenario:

.. code-block:: sql

    SELECT age, race, gender, count(*) AS num FROM stats GROUP TO -1 ORDER BY -1 DESC
    SELECT age, race, gender, count(*) AS num FROM stats GROUP TO 4 ORDER BY -1 DESC
    SELECT age, race, gender, count(*) AS num FROM stats GROUP THROUGH 3 ORDER BY -1 DESC

SQL is often used in an interactive fashion, where data is being explored rather than simply being
gathered. Queries are discovered, rather than being innately known. The pattern usually involves
looking at aggregates (counts, sums, means), while changing both the selection of columns and the
depth to find the most meaningful insights. The frustration in using this pattern is that we often
must change the start of the query (the column list) and also the near end (the grouping indices).
This can be made largely unnecessary by expanding SQL syntax to be more expressive.

sqloose does not validate the correctness of your SQL, but does validate the correctness of the
constructs that are specific to sqloose, including the ranges and use of GROUP TO and GROUP
THROUGH.

Authors
-------

rdj - https://oddacious.github.io

Changelog
---------

0.1.0a1
-------

* Prerelease
