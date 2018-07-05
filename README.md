# cookpad_scrape
Scrape a cookpad profile for all recipes and pictures into a word document, in wikipedia format. 

NOTES:

* Start with: python3 cookpad_russell.py
* Picture download function commented out
* Pictures will download in the folder this script is in
* pythonwikibot command:
    python3 pwb.py pagefromfile -force -file:recipes2.doc

# Output
How the scrape output looks like:

```
{{-start-}}

### --- If Mainpic script used --- ###

[[File:Ananászos sárgarépa torta tojás, olaj, tejtermék és gluténmentesen.jpg]]

### --- /If Mainpic script used --- ###

### --- If Thumb script used --- ###

[[File:Paradicsomos lima bab pirított hagymával.jpg|link=https://cookpad.com/hu/receptek/5285845-paradicsomos-lima-bab-piritott-hagymaval|'''Paradicsomos lima bab pirított hagymával''']]

### --- /If Thumb script used --- ###

'''Ananászos sárgarépa torta tojás, olaj, tejtermék és gluténmentesen'''
=About=


=Ingredients=
* 30 ml darált lenmag
* 75 ml langyos víz
* 110 gr mandulaliszt
* 150 gr gluténmentes liszt
* 15 ml darált fahéj
* 5 ml vanília kivonat
* 5 ml sütőpor
* 5 ml szódabikarbóna
* 40 dkg reszelt sárgarépa
* 22 dkg pépes ananász
* 10 dkg kókuszvirág cukor
* 125 ml almaszósz, natúr
* Az ananászkrémhez:
* 24 dkg nyers kesudió
* 5 ml vaníllia kivonat
* 20 dkg ananász
* A díszítéshez:
* ízlés szerint ananászdarabok
* ízlés szerint kókusz
* A gluténmentes liszthez:
* 240 gr barna rizsliszt
* 96 g burgonya keményitő
* 40 gr fehér rizsliszt
* 30 gr tápióka liszt

=Steps=

[[File:ING-e18f153280174e17-1.jpg|300px|Step 1]]

1. A lenmagot elkeverem a langyos vízzel, majd állni hagyom.

[[File:ING-481f3c1131074d01-2.jpg|300px|Step 2]]

2. A sárgarépát lereszelem.

3. A liszthez valókat kimérem és összekeverem. 15 dkg-ot kimérek és beleteszek egy keverőtálba.

4. A mandulalisztet, sütőport, szódabikarbónát, kókuszcukrot, fahéjat összekeverem a kimért gluténmentes lisztkeverékkel.

5. Hozzáöntöm a lenmagot, vanília kivonatot, sárgarépát, ananászt és kézzel vagy géppel könnyedén összedolgozom.

[[File:ING-b9ab3d77ef836334-6.jpg|300px|Step 6]]

6. A két formát kikenem, a masszát megfelezem és belesimítom a formákba. Ha pontosak akarunk lenni, mérjük le, hogy nagyjából egyforma legyen a mennyiség mindkét formában.

7. 350 F/180 C-on 20 perc alatt megsül. Tűpróba, ha nem ragad semmi sem rá, akkor készen is vagyunk. A formában hagyom hűlni 10 percig, majd kifordítom a formából, ráteszem egy rácsra.

8. Elkészítem a krémet. Egy erős turmixgépben összedarálom a kesut, vaníliát és az ananászt. Ha sűrű, kanalanként adjunk hozzá ananászlevet, hogy könnyen kenhető legyen.

[[File:ING-74feee16339d4b79-9.jpg|300px|Step 9]]

9. A tortalapot jól megkenem a krém felével, ráteszem a másik lapot és a maradék krémet rásimítom a tetejére. Díszítés képen egy kis pirított kókuszreszeléket szórhatok rá.

[[File:ING-30ea53facfd6cf93-10.jpg|300px|Step 10]]

10. Ha lehetőségünk van fahéj fajták között válogatni, a saigoni félét ajánlom erőteljes, csípős, mégis édes íze miatt.

11. A gluténmentes liszt megmaradt részét tegyük félre jól lezárható dobozban.

[[Category:Recipes]]

{{-stop-}}
```

# Screenshot
How a recipe looks after scraping and uploading to mediawiki:

## Mainpic Script
![alt text](https://github.com/pomkos/cookpad_scrape/blob/master/Sample%20-%20import%20to%20wiki%20thumb%20-%20Pineapple%20Carrot%20Cake.jpg)
## Thumb Script
![alt text](https://github.com/pomkos/cookpad_scrape/blob/master/Sample%20-%20import%20to%20wiki%20mainpic%20-%20M%C3%A1ln%C3%A1s%20k%C3%A1v%C3%A9torta%20-%20.jpg)
