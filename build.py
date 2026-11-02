"""Générateur de la maquette Créa'Clair. Usage : python build.py <dossier-du-projet>
Contenus relevés sur la page Facebook de Créa'Clair (novembre 2026). Rien d'inventé : textes, photos, coordonnées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 8  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH, MAIL = '06 27 76 96 52', 'tel:0627769652', 'thomas_clair@hotmail.fr'
FB = 'https://www.facebook.com/p/Creaclair-100064242665990/'

NAV = [('tapis-de-marbre.html', 'Tapis de marbre'), ('piscines.html', 'Piscines'), ('maconnerie.html', 'Maçonnerie'), ('realisations.html', 'Réalisations')]


def pill(t, href, cls='', arrow='↗'):
    return f'<a class="pill {cls}" href="{href}"><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><i><b>CC</b></i><span><em>Créa’</em>Clair</span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('contact.html', 'Devis gratuit', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#0c0c0c">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&family=Great+Vibes&family=Montserrat:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Créa’Clair, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Maçonnerie générale, piscines, tapis de marbre, terrasses sur plots et pavage. Basé à Péronnas, dans l’Ain. Intervention dans l’Ain, le Rhône et la Saône-et-Loire.</p></div>
<div><h4 class="micro">Savoir-faire</h4><ul><li><a href="tapis-de-marbre.html">Tapis de marbre</a></li><li><a href="piscines.html">Piscines</a></li><li><a href="maconnerie.html">Maçonnerie</a></li><li><a href="realisations.html">Réalisations</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="contact.html">Devis gratuit</a></li><li><a href="{FB}" rel="noopener" target="_blank">Facebook</a></li></ul></div>
<div><h4 class="micro">Adresse</h4><ul><li>113 rue du Pic Mar</li><li>01960 Péronnas</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">Créa’Clair</div>
<div class="fb micro"><span class="pad">© Créa’Clair</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Un projet <em>extérieur</em> ?'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Devis gratuit · étude personnalisée</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Demander un devis', 'contact.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def faq(its):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in its) + '</div>'


# photos : r = 2026 (piscine en cours, tapis de marbre à Servas), o = 2022 (tapis de marbre, terrasse et piscine)
GAL = [('o10', 'Marbre', 'Plage de piscine en tapis de marbre'), ('r01', 'Piscine', 'Piscine 7 × 3, escalier décalé'),
       ('o05', 'Marbre', 'Terrasse en tapis de marbre'), ('o07', 'Maçonnerie', 'Terrasse et murets en gabions'),
       ('r02', 'Piscine', 'Bassin en construction'), ('o03', 'Marbre', 'Seuil en tapis de marbre'),
       ('r08', 'Marbre', 'Tapis de marbre à Servas'), ('o08', 'Piscine', 'Piscine et terrasse'),
       ('o01', 'Marbre', 'Allée en tapis de marbre'), ('r04', 'Piscine', 'Escalier décalé'),
       ('o09', 'Maçonnerie', 'Murets éclairés, de nuit'), ('o02', 'Marbre', 'Allée le long de la maison'),
       ('r05', 'Piscine', 'Vue d’ensemble du bassin'), ('o04', 'Marbre', 'Tapis de marbre devant baie vitrée'),
       ('r07', 'Marbre', 'Le grain du marbre, de près'), ('o06', 'Marbre', 'Finition en bordure'),
       ('r03', 'Piscine', 'Angle du bassin'), ('r06', 'Piscine', 'Structure en blocs')]


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def service(file, title, desc, crumb, h1, lead, img, img2, intro_h, intro_p, checks, cat, faqs):
    items = [g for g in GAL if g[1] == cat]
    extra = f'<div class="row rv" style="display:flex;gap:10px;flex-wrap:wrap;margin-top:2.2rem">{pill("Devis gratuit", "contact.html", "blue")}{pill(TEL, TELH, "ghost")}</div>'
    cl = ''.join(f'<li><span><b>{a}</b> {b}</span></li>' for a, b in checks)
    return head(title, desc, file) + pagehead(crumb, h1, lead, img, img2, extra) + f'''
<section class="sec"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Notre savoir-faire</span><h2 class="sp">{intro_h}</h2><p class="lead rv" style="margin-top:1.4rem">{intro_p}</p></div><ul class="checks rv">{cl}</ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Sur nos <em>chantiers</em></h2>{gal(items)}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Questions fréquentes</span><h2 class="sp">On vous <em>répond</em></h2></div><div class="rv">{faq(faqs)}</div></div></section>''' + cta() + foot()


FAQ_ZONE = ('Dans quel secteur intervenez-vous ?', 'Dans l’Ain, le Rhône et la Saône-et-Loire. L’entreprise est basée à Péronnas, près de Bourg-en-Bresse.')
FAQ_DEVIS = ('Le devis est-il gratuit ?', f'Oui. Le devis et l’étude sont gratuits et personnalisés. Appelez le {TEL} ou écrivez-nous.')


def pages():
    P = {}
    hero_tiles = [('t1', 'o10'), ('t2', 'r07'), ('t3', 'o03'), ('t4', 'r01'), ('t5', 'r08'), ('t6', 'o05'), ('t7', 'o07')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['o01', 'o02', 'o03', 'o04', 'o05', 'r08', 'o06', 'o10'])
    wall_imgs = ['o10', 'r01', 'o05', 'o07', 'r02', 'o03', 'o08', 'o01', 'r04', 'o02', 'r05', 'o04', 'o06', 'r07', 'o09']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('tapis-de-marbre.html', '01', 'Tapis de marbre', 'Résine drainante, esthétique et durable. Dehors comme dedans.', 'r08'),
             ('piscines.html', '02', 'Piscines', 'Construction et rénovation, de la conception à la réalisation.', 'r01'),
             ('maconnerie.html', '03', 'Maçonnerie', 'Constructions neuves, agrandissements, rénovations.', 'o07'),
             ('maconnerie.html#terrasses', '04', 'Terrasses', 'Terrasses sur plots, pavage, aménagements paysagers.', 'o10')]
    pl = ''.join(f'<a href="{h}"><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>Devis gratuit</b></span></a>' for h, n, t, d, _ in items)
    prev = ''.join(tile(f'{PH}{im}.webp', 'on' if i == 0 else '') for i, (*_, im) in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [('r01', 'Escalier décalé'), ('r05', 'Bassin 7 × 3'), ('r02', 'Côté maison'), ('r04', 'Les marches'), ('r03', 'Angle du bassin'), ('r06', 'Structure en blocs')])
    steps = [('Votre appel', f'Un coup de fil au {TEL}, un message ou un e-mail. Vous décrivez votre projet.'),
             ('Étude et devis', 'Une étude personnalisée de votre projet terrasse, piscine ou maçonnerie. Devis gratuit.'),
             ('Réalisation', 'De la conception à la réalisation, un seul interlocuteur pour votre chantier.'),
             ('Finitions', 'Un travail soigné et des finitions de haute qualité.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Tapis de marbre', 'Piscines', 'Maçonnerie', 'Terrasses sur plots', 'Pavage', 'Résine drainante'] * 2)
    zones = [('ain', 'Ain', 'Péronnas, Bourg-en-Bresse, Servas…', '01'), ('rhone', 'Rhône', 'Sur demande, devis gratuit.', '69'), ('saone', 'Saône-et-Loire', 'Sur demande, devis gratuit.', '71')]
    zl = '<div class="agl">' + ''.join(f'<article class="row"><h3>{n}</h3><address>{a}</address><span class="dep micro">{d}</span><a class="tel" href="{TELH}">{TEL}</a></article>' for _, n, a, d in zones) + '</div>'

    P['index.html'] = head('Créa’Clair — Tapis de marbre, piscines et maçonnerie à Péronnas (Ain)', 'Créa’Clair, artisan à Péronnas : tapis de marbre, construction de piscines, maçonnerie générale, terrasses sur plots et pavage. Ain, Rhône, Saône-et-Loire. Devis gratuit.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Marbre · Piscines</b>Maçonnerie à Péronnas</div>
<div class="cap micro c2"><b>Devis gratuit</b>Étude personnalisée</div>
<div class="cap micro c3"><b>Ain · Rhône</b>Saône-et-Loire</div>
<div class="go">{pill('Devis gratuit', 'contact.html')}</div>
{ht}
<p class="para">Sublimez vos extérieurs. Marbre, piscine, maçonnerie : un seul artisan.</p>
<h1 class="word">Créa’Clair</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Pourquoi choisir Créa’Clair ?</span><h2 class="sp">Votre <em>partenaire unique</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Au-delà de la maçonnerie, nous créons des tapis de marbre et des piscines. Pour transformer vos espaces avec élégance et fonctionnalité.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Travail soigné.</b> Des finitions de haute qualité.</span></li><li><span><b>Sur mesure.</b> Des solutions personnalisées pour vos projets terrasse et piscine.</span></li><li><span><b>Devis gratuit.</b> Et une étude personnalisée.</span></li></ul>{pill('Voir nos réalisations', 'realisations.html', 'blue')}</div>{tile(PH + 'o08.webp', '', par=8, alt='Piscine et terrasse réalisées par Créa’Clair')}</div></section>

<section class="story"><span class="micro mute m3">Le tapis de marbre</span>
<h2><span class="w">Sublimez</span> <span class="w">vos</span> <span class="w">extérieurs</span> <span class="w">avec</span> <span class="w">l’élégance</span> <span class="w">du</span> <span class="w"><em>marbre</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Résine drainante, esthétique et durable. Allées, terrasses, plages de piscine, seuils.</p><span class="micro mute m2">Dehors comme dedans</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">De la conception à la réalisation</span><h2>Vos extérieurs, <em>transformés</em></h2>{pill('Voir les réalisations', 'realisations.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Nos savoir-faire</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Que voulez-vous <em>créer ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Chantier d’octobre 2026</span><h2>Une piscine 7 × 3, <em>escalier décalé</em></h2></div>{pill('Nos piscines', 'piscines.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre projet</span><h2 class="sp">Du premier appel <em>aux finitions</em></h2><div class="steps">{st}</div></div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:flex-end;gap:2rem;flex-wrap:wrap;margin-bottom:clamp(2rem,5vw,4rem)"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Secteur d’intervention</span><h2 class="sp">Trois départements, <em>un artisan</em></h2></div>{pill('Nous contacter', 'contact.html', 'ghost')}</div>{zl}</div></section>
{cta()}''' + foot()

    P['tapis-de-marbre.html'] = service('tapis-de-marbre.html', 'Tapis de marbre et résine — Créa’Clair, Péronnas (Ain)', 'Pose de tapis de marbre (résine de marbre) pour allées, terrasses, plages de piscine et intérieurs. Drainant, esthétique, durable. Ain, Rhône, Saône-et-Loire.',
        'Tapis de marbre', 'Le tapis <em>de marbre</em>', 'Une résine drainante, esthétique et durable. Pour des surfaces élégantes et personnalisables, dehors comme dedans.', PH + 'r08.webp', PH + 'o10.webp',
        'Un revêtement <em>moderne</em>', 'Forts de notre expérience de la résine, nous posons des tapis de marbre sur vos allées, terrasses, plages de piscine et seuils.',
        [('Drainant.', 'L’eau s’infiltre au lieu de stagner.'), ('Esthétique.', 'Le grain du marbre, élégant et lumineux.'), ('Durable.', 'Un revêtement fait pour durer.'), ('Personnalisable.', 'Extérieur ou intérieur, selon votre projet.')], 'Marbre',
        [('Peut-on poser un tapis de marbre à l’intérieur ?', 'Oui. Le tapis de marbre convient aux surfaces extérieures comme intérieures.'), ('Où le poser ?', 'Allées, terrasses, plages de piscine, seuils de porte : nos réalisations en montrent plusieurs exemples.'), FAQ_DEVIS, FAQ_ZONE])

    P['piscines.html'] = service('piscines.html', 'Construction de piscines — Créa’Clair, Péronnas (Ain)', 'Construction et rénovation de piscines, de la conception à la réalisation. Plages en tapis de marbre. Ain, Rhône, Saône-et-Loire. Devis gratuit.',
        'Piscines', 'Votre piscine, <em>sur mesure</em>', 'Construction et rénovation, de la conception à la réalisation. Pour une oasis de fraîcheur chez vous.', PH + 'o08.webp', PH + 'r01.webp',
        'De la conception <em>à la réalisation</em>', 'Dernier chantier en date : une piscine 7 × 3 avec escalier décalé, pour un rendu moderne et élégant.',
        [('Construction.', 'Structure maçonnée, sur mesure.'), ('Rénovation.', 'Redonnez vie à votre bassin.'), ('Plages en marbre.', 'Un tour de piscine drainant et élégant.'), ('Un seul artisan.', 'Maçonnerie, piscine et abords.')], 'Piscine',
        [('Construisez-vous aussi les abords ?', 'Oui : plage en tapis de marbre, terrasse, murets et maçonnerie autour du bassin.'), FAQ_DEVIS, FAQ_ZONE])

    P['maconnerie.html'] = service('maconnerie.html', 'Maçonnerie générale et terrasses — Créa’Clair, Péronnas (Ain)', 'Maçonnerie générale : constructions neuves, agrandissements, rénovations. Terrasses sur plots, pavage, aménagements paysagers. Ain, Rhône, Saône-et-Loire.',
        'Maçonnerie', 'Construire, <em>agrandir</em>, rénover', 'Maçonnerie générale, terrasses sur plots, pavage et aménagements paysagers.', PH + 'o07.webp', PH + 'o09.webp',
        'Tous vos <em>travaux</em>', 'Constructions neuves, agrandissements, rénovations : contactez-nous pour en parler. Devis gratuit.',
        [('Constructions neuves.', 'Du gros œuvre aux finitions.'), ('Agrandissements.', 'Gagnez de la place chez vous.'), ('Rénovations.', 'Remise en état et modernisation.'), ('Terrasses et pavage.', 'Terrasses sur plots, pavés, murets, aménagements paysagers.')], 'Maçonnerie',
        [FAQ_DEVIS, FAQ_ZONE]).replace('<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations', '<section class="sec" id="terrasses" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réalisations', 1)

    P['realisations.html'] = head('Réalisations — Créa’Clair', 'Photos de chantiers Créa’Clair : tapis de marbre, piscines, maçonnerie et terrasses dans l’Ain.', 'realisations.html') + pagehead('Réalisations', 'Nos <em>réalisations</em>', 'Tapis de marbre, piscines, terrasses : quelques chantiers récents, en photos.', PH + 'o10.webp', PH + 'r07.webp') + f'''
<section class="sec"><div class="wrap"><div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="Marbre">Tapis de marbre</button><button data-f="Piscine">Piscines</button><button data-f="Maçonnerie">Maçonnerie</button></div>{gal(GAL)}<p class="note" style="margin-top:2rem">Photos publiées par Créa’Clair sur sa page Facebook.</p></div></section>''' + cta() + foot()

    P['contact.html'] = head('Contact et devis gratuit — Créa’Clair', f'Demandez votre devis gratuit à Créa’Clair : {TEL}, {MAIL}. 113 rue du Pic Mar, 01960 Péronnas.', 'contact.html') + pagehead('Contact', 'Parlons de <em>votre projet</em>', 'Devis gratuit et étude personnalisée. Ain, Rhône et Saône-et-Loire.', PH + 'o05.webp') + f'''
<section class="sec" id="contact"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Coordonnées</span><h2 class="sp">Un appel <em>suffit</em></h2>
<div class="contactline rv" style="margin-top:2rem"><a href="{TELH}">{TEL}</a><a href="mailto:{MAIL}">{MAIL}</a></div>
<p class="lead rv" style="margin-top:1.6rem">113 rue du Pic Mar<br>01960 Péronnas</p></div>
<form class="f calc rv"><div class="r2"><div class="fld"><label for="n">Nom</label><input id="n" required></div><div class="fld"><label for="t">Téléphone</label><input id="t" type="tel" required></div></div>
<div class="fld"><label for="e">E-mail</label><input id="e" type="email"></div>
<div class="r2"><div class="fld"><label for="p">Projet</label><select id="p"><option>Tapis de marbre</option><option>Piscine</option><option>Maçonnerie</option><option>Terrasse ou pavage</option><option>Autre</option></select></div><div class="fld"><label for="v">Commune</label><input id="v"></div></div>
<div class="fld"><label for="m">Votre projet en quelques mots</label><textarea id="m" rows="4" placeholder="Surface, délai, photos à envoyer…"></textarea></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Envoyer</span><span>Envoyer</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucun message n’est envoyé.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
