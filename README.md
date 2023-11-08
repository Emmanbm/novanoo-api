# L'API est déployée sur VERCEL

<h3>Les fichiers sont lus à partir de la racine du projet, raison pour laquelle les importations et lectures des fichiers doivent se faire à partir de la racine du projet dans les fichiers python.</h3>

<p>Cela ne fonctionnerait pas en local. Pour les tests en local, les importations doivent se faire à partir de la racine de <b>app.py</b>.</p>

<p>Par exemple: Pour l'importation de functions.py dans app.py</p>
<p>Pour le déploiement on fait</p>
<pre>
import api.objects.functions
<pre>
<p>Pour les tests en local on fait</p>
<pre>
import objects.functions
<pre>