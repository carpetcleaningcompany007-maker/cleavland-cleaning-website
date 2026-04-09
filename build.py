from pathlib import Path
root = Path('/mnt/data/cleveland_rebuild')

def header(title, desc, depth=''):
    prefix = depth
    return f'''<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<div class="topbar"><div class="container"><div>25 years • Cleaning Perfection</div><div>All cleaning enquiries • 01952 585588</div></div></div>
<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="{prefix}index.html"><span class="brand-badge">CC</span><span>Cleveland Cleaning<small>Commercial & Specialist Cleaning</small></span></a>
    <nav class="nav" aria-label="Primary navigation">
      <a class="nav-link" href="{prefix}index.html">Home</a>
      <div class="nav-item"><a class="nav-link" href="{prefix}cleaning-services/index.html">Cleaning Services</a>
        <div class="dropdown">
          <a href="{prefix}cleaning-services/commercial-cleaning/index.html">Commercial Cleaning</a>
          <a href="{prefix}cleaning-services/commercial-cleaning/office-cleaning.html">Office Cleaning</a>
          <a href="{prefix}cleaning-services/commercial-cleaning/carpet-cleaning.html">Carpet Cleaning</a>
          <a href="{prefix}cleaning-services/specialist-cleaning/builders-clean.html">Builders Clean</a>
          <a href="{prefix}cleaning-services/specialist-cleaning/high-level-cleaning.html">High Level Cleaning</a>
        </div>
      </div>
      <div class="nav-item"><a class="nav-link" href="{prefix}why-choose-us.html">About</a>
        <div class="dropdown">
          <a href="{prefix}why-choose-us.html">Why Choose Us</a>
          <a href="{prefix}meet-the-team.html">Meet the Team</a>
          <a href="{prefix}about.html">Our Values</a>
        </div>
      </div>
      <div class="nav-item"><a class="nav-link" href="{prefix}locations/cleaning-in-telford.html">Locations</a>
        <div class="dropdown">
          <a href="{prefix}locations/cleaning-in-telford.html">Cleaning in Telford</a>
          <a href="{prefix}locations/cleaning-in-shrewsbury.html">Cleaning in Shrewsbury</a>
          <a href="{prefix}locations/cleaning-in-ludlow.html">Cleaning in Ludlow</a>
        </div>
      </div>
      <a class="nav-link" href="{prefix}contact-us.html">Contact Us</a>
    </nav>
    <a class="cta-btn" href="{prefix}contact-us.html">Request a Quote</a>
  </div>
</header>
'''

def footer(depth=''):
    prefix=depth
    return f'''
<footer class="footer">
  <div class="container">
    <div class="footer-cols">
      <div><h4>Contact</h4><p>01952 585588<br>enquiries@clevelandcleaning.co.uk</p></div>
      <div><h4>Office</h4><p>Unit G8 Court Works Industrial Estate<br>Bridgnorth Road<br>Madeley, Telford<br>Shropshire TF7 4JB</p></div>
      <div><h4>Sectors</h4><a href="#">Construction</a><a href="#">Industrial Cleaning</a><a href="#">Medical Practice Cleaning</a><a href="#">Office & Commercial Cleaning</a></div>
      <div><h4>Locations</h4><a href="{prefix}locations/cleaning-in-telford.html">Cleaning Services in Telford</a><a href="{prefix}locations/cleaning-in-shrewsbury.html">Cleaning Services in Shrewsbury</a><a href="{prefix}locations/cleaning-in-ludlow.html">Cleaning Services in Ludlow</a><a href="{prefix}contact-us.html">Contact Us</a></div>
    </div>
    <div class="footer-bottom"><span>© Cleveland Cleaning Limited 2026</span><span>Family run cleaning company across Shropshire and the West Midlands</span></div>
  </div>
</footer>
</body></html>'''


def pagehero(title, text, crumbs, depth=''):
    return f'''<section class="page-hero"><div class="container"><div class="breadcrumbs">{crumbs}</div><h1>{title}</h1><p>{text}</p></div></section>'''

pages = {}

pages['index.html'] = header('Cleveland Cleaning: Commercial & Specialist Cleaning Services','Commercial and specialist cleaning services across Shropshire and the West Midlands.') + '''
<section class="hero">
  <div class="container">
    <div>
      <span class="kicker">At your side every step of the way</span>
      <h1>Providing Commercial and Specialist Cleaning Services Across Shropshire and the West Midlands for more than 25 years.</h1>
      <p class="lead">Professional, family run cleaning for offices, factories, medical centres, schools, housing, carpet cleaning and specialist one off projects.</p>
      <div class="actions">
        <a class="cta-btn" href="contact-us.html">Request my FREE quotation</a>
        <a class="btn alt" href="cleaning-services/index.html">Explore our services</a>
      </div>
    </div>
    <div class="hero-card">
      <h3 style="margin-top:0;font-size:30px">Cleveland Cleaning Guarantee</h3>
      <p>If you are not completely happy with our work, we’ll come back and fix it. If things are still not up to your standards you won’t pay a penny.</p>
      <ul class="tick-list">
        <li>Fully employed and trained staff</li>
        <li>Senior team reviews and regular audits</li>
        <li>Flexible cleaning around your opening hours</li>
        <li>ISO accredited working standards</li>
      </ul>
    </div>
  </div>
</section>
<section class="container stats">
  <div class="stat"><strong>25+</strong><span>Years experience</span></div>
  <div class="stat"><strong>5★</strong><span>Cleveland standard</span></div>
  <div class="stat"><strong>100s</strong><span>Commercial clients supported</span></div>
  <div class="stat"><strong>Local</strong><span>West Midlands coverage</span></div>
</section>
<section class="section"><div class="container">
  <h2>Who we work with</h2>
  <p class="section-intro">We support offices, schools, factories, healthcare settings, housing providers and commercial premises with dependable scheduled and specialist cleaning.</p>
  <div class="logo-row">
    <div class="logo">NHS</div><div class="logo">Ramada</div><div class="logo">Lyreco</div><div class="logo">Magna</div><div class="logo">Reconomy</div>
  </div>
</div></section>
<section class="section alt"><div class="container split">
  <div>
    <h2>At Cleveland Cleaning you will experience</h2>
    <div class="checks">
      <div class="check">The same friendly, professional members of staff</div>
      <div class="check">Senior team site visits and review meetings</div>
      <div class="check">Fully trained staff across every cleaning service</div>
      <div class="check">Open communication and client portal style reporting</div>
    </div>
  </div>
  <div class="image-panel"></div>
</div></section>
<section class="section"><div class="container">
  <h2>Our cleaning services</h2>
  <div class="grid grid-3">
    <article class="card"><h3>Commercial Cleaning</h3><p>Office cleaning, contract cleaning, carpet cleaning, industrial cleaning, window cleaning and more for busy workplaces.</p><a class="btn alt" href="cleaning-services/commercial-cleaning/index.html">View commercial services</a></article>
    <article class="card"><h3>Specialist Cleaning</h3><p>Builders cleans, end of tenancy, student accommodation, clinical cleaning, event cleaning, car park cleaning and high level work.</p><a class="btn alt" href="cleaning-services/specialist-cleaning/builders-clean.html">View specialist services</a></article>
    <article class="card"><h3>Coverage Area</h3><p>Shrewsbury, Telford, Ludlow, Oswestry and across the West Midlands with bespoke packages for every site.</p><a class="btn alt" href="locations/cleaning-in-telford.html">See locations</a></article>
  </div>
</div></section>
<section class="section alt"><div class="container">
  <div class="band">
    <div><h2 style="color:#fff;margin-top:0">Do we cover your area?</h2><p>Our exceptional team service clients across Shrewsbury, Telford, Oswestry, Ludlow and into the West Midlands with bespoke commercial and contract cleaning packages.</p></div>
    <div class="area-links">
      <a href="locations/cleaning-in-telford.html">Telford</a>
      <a href="locations/cleaning-in-shrewsbury.html">Shrewsbury</a>
      <a href="locations/cleaning-in-ludlow.html">Ludlow</a>
      <a href="contact-us.html">Request a quote</a>
    </div>
  </div>
</div></section>
<section class="section"><div class="container"><div class="quote-strip"><div><h2 style="color:#fff;margin:0 0 8px">Request your FREE on site visit from our professional and friendly team today.</h2><p style="margin:0;color:#ecf5ff">Tell us about your site and we’ll arrange the right service at the right time.</p></div><a class="cta-btn" href="contact-us.html">Request your FREE quotation</a></div></div></section>
''' + footer()

services_intro = '''Over 25 years experience, West Midlands coverage, all sites regularly audited and ISO accredited standards across every contract.'''

pages['cleaning-services/index.html'] = header('Cleaning Services | Cleveland Cleaning', services_intro, '../') + pagehero('Cleaning Services', 'Our priority is providing an unparalleled cleaning experience from the first moment you choose us.', '<a href="../index.html">Home</a> / Cleaning Services', '../') + '''
<section class="section"><div class="container">
  <div class="grid grid-3">
    <article class="card"><h3>Commercial Cleaning</h3><p>Reliable, flexible support for offices, communal spaces, factories and contract sites.</p><ul class="tick-list"><li>Office cleaning</li><li>Carpet cleaning</li><li>Contract cleaning</li><li>Industrial cleaning</li></ul><a class="btn alt" href="commercial-cleaning/index.html">Read more</a></article>
    <article class="card"><h3>Specialist Cleaning</h3><p>One off and technical cleaning projects carried out by trained staff with specialist equipment.</p><ul class="tick-list"><li>Builders cleans</li><li>Clinical cleaning</li><li>High level cleaning</li><li>Warehouse cleaning</li></ul><a class="btn alt" href="specialist-cleaning/builders-clean.html">Read more</a></article>
    <article class="card"><h3>Free Quotations</h3><p>Whether you are in Telford, Shrewsbury, Wolverhampton or anywhere in between, we’ll happily visit and price your requirements.</p><a class="btn alt" href="../contact-us.html">Request a quote</a></article>
  </div>
</div></section>
''' + footer('../')

pages['cleaning-services/commercial-cleaning/index.html'] = header('Commercial Cleaning | Cleveland Cleaning', 'Commercial cleaning services for offices and workplaces.', '../../') + pagehero('Commercial Cleaning', 'Professional commercial cleaning for busy sites that need dependable standards, flexible hours and a team that takes pride in every clean.', '<a href="../../index.html">Home</a> / <a href="../index.html">Cleaning Services</a> / Commercial Cleaning', '../../') + '''
<section class="section"><div class="container grid grid-3">
<article class="card"><h3>Office Cleaning</h3><p>Daily, weekly and bespoke office cleaning planned around your staff and opening hours.</p><a class="btn alt" href="office-cleaning.html">Office cleaning</a></article>
<article class="card"><h3>Carpet Cleaning</h3><p>Commercial carpet cleaning for offices, communal areas and contract sites with specialist equipment.</p><a class="btn alt" href="carpet-cleaning.html">Carpet cleaning</a></article>
<article class="card"><h3>Industrial Cleaning</h3><p>Machinery, mezzanines, hard floors, production areas and deeper site support when you need it.</p><a class="btn alt" href="industrial-cleaning.html">Industrial cleaning</a></article>
</div></section>
''' + footer('../../')

subpages = {
 'cleaning-services/commercial-cleaning/office-cleaning.html':('Office Cleaning','Our office cleaning service allows you to relax knowing that high quality cleaning is underway before your team arrives or after everyone has gone home.'),
 'cleaning-services/commercial-cleaning/carpet-cleaning.html':('Carpet Cleaning','Commercial carpet cleaning for offices, corridors and communal areas using trained staff and specialist machinery for a fresher, cleaner workplace.'),
 'cleaning-services/commercial-cleaning/industrial-cleaning.html':('Industrial Cleaning','From hard flooring in factories to pipework, machinery, mezzanine structures and production lines, our team has cleaned them all.'),
 'cleaning-services/specialist-cleaning/builders-clean.html':('Builders Clean','Detailed post build and sparkle cleans to get new spaces ready for handover, occupation or opening day.'),
 'cleaning-services/specialist-cleaning/high-level-cleaning.html':('High Level Cleaning','Our IPAF trained staff have the equipment, qualifications and passion to clean those hard to reach high areas safely and thoroughly.'),
 'cleaning-services/specialist-cleaning/clinical-cleaning.html':('Clinical Cleaning','Our team promotes the highest cleaning and hygiene standards to meet industry specific regulations in medical and clinical environments.')
}
for path,(title,text) in subpages.items():
    depth = '../../' if path.count('/')==3 else '../'
    crumbs = '<a href="../../index.html">Home</a> / <a href="../index.html">Cleaning Services</a>' if depth=='../../' else '<a href="../index.html">Home</a>'
    pages[path] = header(f'{title} | Cleveland Cleaning', text, '../../') + pagehero(title, text, '<a href="../../index.html">Home</a> / <a href="../index.html">Cleaning Services</a>', '../../') + f'''
<section class="section"><div class="container split"><div>
  <h2>{title}</h2><p class="section-intro">{text}</p>
  <ul class="tick-list"><li>Flexible scheduling around your site</li><li>Trained and fully employed staff</li><li>Regular audits and review meetings</li><li>Free site visit and quotation</li></ul>
  <div class="actions"><a class="cta-btn" href="../../contact-us.html">Request a quote</a><a class="btn alt" href="../../why-choose-us.html">Why choose us</a></div>
</div><div class="image-panel"></div></div></section>
''' + footer('../../')

pages['why-choose-us.html'] = header('Why Choose Us | Cleveland Cleaning', 'Family run cleaning company serving Shropshire and the West Midlands.') + pagehero('Why Choose Us', 'As an independent, family run cleaning business, we are proud to service the private and public sectors and commercial premises across Shropshire and the West Midlands.', '<a href="index.html">Home</a> / Why Choose Us') + '''
<section class="section"><div class="container grid grid-3">
  <div class="card"><h3>Our mission</h3><p>We are consistent in our provision of cleaning services ensuring that they are always of the highest possible quality.</p></div>
  <div class="card"><h3>Our approach</h3><p>We build strong, long lasting client relationships and aim to deliver exceptional service every single time.</p></div>
  <div class="card"><h3>Our standards</h3><p>Honesty, transparency, regular audits, open communication and pride in every finished result.</p></div>
</div></section>
''' + footer()

pages['about.html'] = header('Our Values | Cleveland Cleaning', 'Our values and standards.') + pagehero('Our Values', 'High quality service every time. Consistent approach to every job. Open door policy for staff and customers because communication is key to success.', '<a href="index.html">Home</a> / Our Values') + '''
<section class="section"><div class="container split"><div>
<h2>What we stand for</h2>
<ul class="tick-list"><li>Honesty and transparency</li><li>High quality service every time</li><li>Consistent approach to every job</li><li>Open communication with staff and customers</li><li>Mentoring the next generation of cleaners and managers</li></ul>
</div><div class="form-card"><h3>Built for long term partnerships</h3><p>We take pride in dependable service, clear standards and teams that care about doing the job properly.</p></div></div></section>
''' + footer()

pages['meet-the-team.html'] = header('Meet the Team | Cleveland Cleaning', 'Meet the Cleveland Cleaning team.') + pagehero('Meet the Team', 'Friendly faces, strong standards and a genuine pride in helping our clients keep their premises clean, safe and presentable.', '<a href="index.html">Home</a> / Meet the Team') + '''
<section class="section"><div class="container team-grid">
  <article class="team-card"><div class="photo"></div><div class="content"><h3>Amanda</h3><p><strong>Operations Director</strong></p><p>Amanda keeps contracts moving smoothly and loves building long standing client relationships that grow over time.</p></div></article>
  <article class="team-card"><div class="photo"></div><div class="content"><h3>Jane</h3><p><strong>Chief Relief Worker</strong></p><p>There isn’t a Cleveland Cleaning contract Jane doesn’t know. She loves getting stuck into detailed builders cleans.</p></div></article>
  <article class="team-card"><div class="photo"></div><div class="content"><h3>Chris</h3><p><strong>Senior Supervisor</strong></p><p>Chris leads audits, site reviews and keeps quality high across a wide range of commercial and specialist jobs.</p></div></article>
</div></section>
''' + footer()

for slug, place in [('locations/cleaning-in-telford.html','Telford'),('locations/cleaning-in-shrewsbury.html','Shrewsbury'),('locations/cleaning-in-ludlow.html','Ludlow')]:
    pages[slug] = header(f'Cleaning Services in {place} | Cleveland Cleaning', f'Cleaning services in {place}.', '../') + pagehero(f'Cleaning Services in {place}', f'Cleveland Cleaning has been proud to provide office, commercial and specialist cleaning services in {place} with consistent and reliable standards for companies of all sizes.', f'<a href="../index.html">Home</a> / Cleaning in {place}', '../') + f'''
<section class="section"><div class="container split"><div>
  <h2>Professional cleaning in {place}</h2>
  <p class="section-intro">A clean workspace is crucial whether you run an office, restaurant, medical practice, school or industrial site. Our cleaning services in {place} give businesses professional standard results backed by over 25 years of experience.</p>
  <ul class="tick-list"><li>Office and commercial cleaning</li><li>Specialist one off cleaning projects</li><li>Free quotations and flexible scheduling</li><li>Trained staff and specialist equipment</li></ul>
</div><div class="form-card"><h3>Need help in {place}?</h3><p>From one off office cleaning to commercial floor cleaning and wider site support, our team is ready to help.</p><a class="cta-btn" href="../contact-us.html">Request your FREE quotation</a></div></div></section>
''' + footer('../')

pages['contact-us.html'] = header('Contact Us | Cleveland Cleaning', 'Get in touch with our team today to discuss your cleaning needs.') + pagehero('Contact Us', 'Get in touch with our team today to discuss your cleaning needs and request your free quotation.', '<a href="index.html">Home</a> / Contact Us') + '''
<section class="section"><div class="container split">
  <div class="form-card"><h2 style="margin-top:0">Request your FREE quotation</h2>
    <form>
      <input type="text" placeholder="Name" required>
      <input type="tel" placeholder="Contact Number" required>
      <input type="email" placeholder="Email Address" required>
      <input type="text" placeholder="Postcode" required>
      <textarea placeholder="How can we help?"></textarea>
      <button class="cta-btn" type="submit">Send enquiry</button>
    </form>
  </div>
  <div>
    <div class="card"><h3>Call Us</h3><p>01952 585588</p></div>
    <div class="card"><h3>Email Us</h3><p>enquiries@clevelandcleaning.co.uk</p></div>
    <div class="card"><h3>Find Us</h3><p>Unit G8 Court Works Industrial Estate<br>Bridgnorth Road<br>Madeley, Telford<br>Shropshire TF7 4JB</p></div>
  </div>
</div></section>
''' + footer()

for path, content in pages.items():
    full = root / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding='utf-8')
print(f'wrote {len(pages)} pages')
