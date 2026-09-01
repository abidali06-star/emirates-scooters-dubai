import React from 'react';
import Link from 'next/link';

export default function HomePage() {
  const homeFaqs = [
    {
      q: 'How much does an electric scooter cost in Dubai?',
      a: 'Our in-stock range is 699 AED for the Mankeel MK083 and 1,499 AED for the MX-14, VAT inclusive with free local delivery. Comparable scooters at UAE retailers run from around 685 AED at entry level to over 2,000 AED for high-power models.',
    },
    {
      q: 'Is it legal to ride an electric scooter in Dubai?',
      a: 'Yes, on designated tracks and shared paths, with a free RTA permit for riders aged 16 and over who do not hold a UAE driving licence. RTA requires an e-scooter maximum speed of 20 km/h. Both our models have three speed modes, with mode 1 limited to 20 km/h.',
    },
    {
      q: 'Which Mankeel model should I buy?',
      a: 'The MK083 (699 AED, 12 kg) if you commute on paved paths and want something light enough to fold and carry, including onto the Metro. The MX-14 (1,499 AED, 18 kg) if you want more range, more power, dual suspension and off-road tyres.',
    },
    {
      q: 'Do you deliver, and can I see the scooter first?',
      a: 'Yes to both. We have no shop &mdash; we bring the scooter to you and hand it over in person, so you can inspect it before you accept it. Free delivery across Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community and JVT.',
    },
    {
      q: 'How far will it go on one charge?',
      a: 'The MK083 is rated 35 km and the MX-14 is rated 56 km. Expect roughly 70&ndash;80% of the rated figure in Dubai summer, depending on rider weight, speed mode and terrain.',
    },
    {
      q: 'Is there a warranty and can you service it?',
      a: 'One year in the UAE. We service what we sell and hold genuine Mankeel spare parts locally, so a brake lever or charger does not mean shipping the scooter overseas.',
    },
    {
      q: 'Will the battery cope with Dubai summer?',
      a: 'Yes, with care. Do not charge straight after riding &mdash; let the pack cool for 30 to 45 minutes indoors first. Store between 20% and 80% charge, out of direct sun. We check battery health at delivery.',
    },
  ];

  const products = [
    { id: 'mk083', model: 'MK083', name: 'Mankeel MK083 City Commuter (350W)', price: '699 AED', inStock: true, desc: 'Compact 350W commuter scooter with solid honeycomb tires, cruise control, and fast folding.' },
    { id: 'mx-14', model: 'MX-14', name: 'Mankeel MX-14 Off-Road (800W)', price: '1,499 AED', inStock: true, desc: 'Heavy-duty 800W off-road scooter with dual spring suspensions, 10" off-road tires, and 56 KM range.' }
  ];

  return (
    <div className="max-w-5xl mx-auto p-8 font-sans">
      <header className="bg-slate-900 text-white p-8 rounded-xl mb-8 shadow-lg">
        <span className="bg-emerald-500 text-white text-xs px-3 py-1 rounded-full font-bold">
          Official Dubai Store
        </span>
        <h1 className="text-3xl font-bold mt-3">Emirates E-Scooters</h1>
        <p className="text-slate-300 mt-2">
          Official Dubai catalog of Mankeel electric scooters, with local summer warranty and free delivery across Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community, and JVT.
        </p>
      </header>

      <section className="mb-10">
        <h2 className="text-2xl font-bold mb-6 text-slate-800">Featured Active Models</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {products.map((p) => (
            <div key={p.id} className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-bold text-slate-500">Mankeel {p.model}</span>
                  <span className="bg-emerald-500 text-white text-xs px-2.5 py-0.5 rounded-full font-bold">
                    In Stock
                  </span>
                </div>
                <h3 className="font-bold text-xl text-slate-900">{p.name}</h3>
                <p className="text-slate-600 text-sm mt-2">{p.desc}</p>
                <p className="text-blue-600 font-extrabold text-2xl mt-4">{p.price}</p>
              </div>
              <Link
                href={`/products/${p.id}`}
                className="block text-center mt-6 text-sm bg-slate-900 text-white px-4 py-3 rounded-lg font-semibold hover:bg-slate-800 transition shadow"
              >
                View Full Specifications & Schema
              </Link>
            </div>
          ))}
        </div>
      </section>

      <section className="mb-10 bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
        <h2 className="text-xl font-bold text-slate-900 mb-3">Why buy a Mankeel from us</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-slate-700">
          <div className="p-4 bg-slate-50 rounded-lg border border-slate-100">
            <h3 className="font-bold text-slate-900 mb-1">Solid puncture-proof tyres</h3>
            <p>
              The MK083 runs solid honeycomb tyres. There is no inner tube to puncture on hot
              Dubai asphalt, and nothing to re-inflate.
            </p>
          </div>
          <div className="p-4 bg-slate-50 rounded-lg border border-slate-100">
            <h3 className="font-bold text-slate-900 mb-1">About 20% less on like-for-like spec</h3>
            <p>
              The MX-14 is 1,499 AED. The closest 45 km/h dual-suspension scooter we found on sale
              in the UAE was 1,885 AED &mdash; and ours carries more range (56 km vs 50 km) and
              weighs 5 kg less. <span className="text-slate-500">UAE retail prices checked September 2026.</span>
            </p>
          </div>
          <div className="p-4 bg-slate-50 rounded-lg border border-slate-100">
            <h3 className="font-bold text-slate-900 mb-1">1-year UAE warranty, and we come to you</h3>
            <p>
              Genuine Mankeel spare parts held locally, battery health checks, and free delivery
              across 11 Dubai communities. You inspect the scooter in person before you accept it.
            </p>
          </div>
        </div>
      </section>

      <section className="bg-emerald-50 p-6 rounded-xl border border-emerald-200">
        <h2 className="text-xl font-bold text-emerald-900 mb-2">Dubai Local Authority Hub & RTA Compliance</h2>
        <ul className="space-y-2 text-emerald-800 text-sm font-medium">
          <li>• <strong>RTA Permit Guide:</strong> How to obtain your free Dubai e-scooter permit online.</li>
          <li>• <strong>Summer Heat Care:</strong> Protecting lithium batteries in 45°C+ UAE summer heat.</li>
          <li>• <strong>Track Maps:</strong> Designated tracks in JLT, Dubai Water Canal, Business Bay & Downtown Dubai.</li>
          <li>• <strong>Brand Comparison Guide:</strong> <Link href="/blogs/best-electric-scooters-dubai-comparison" className="underline hover:text-emerald-950">Mankeel vs Xiaomi & Ninebot Comparison</Link></li>
        </ul>
      </section>

      <section className="mt-10 bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
        <h2 className="text-xl font-bold text-slate-900 mb-4">Buying an electric scooter in Dubai &mdash; common questions</h2>
        {homeFaqs.map((f, i) => (
          <div key={i} className="mb-4">
            <h3 className="text-sm font-semibold text-slate-900">{f.q}</h3>
            <p className="text-sm text-slate-700 mt-1">{f.a}</p>
          </div>
        ))}
        <p className="mt-4 text-sm">
          More photos of every model are on our{' '}
          <a
            href="https://www.facebook.com/profile.php?id=61582981335703"
            target="_blank"
            rel="noopener noreferrer"
            className="font-medium text-blue-700 underline"
          >
            Facebook page
          </a>
          . Questions? Call or WhatsApp <strong>+971 56 667 2354</strong>, 08:00&ndash;22:00 daily.
        </p>
      </section>

      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{
          __html: JSON.stringify({
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            mainEntity: homeFaqs.map((f) => ({
              '@type': 'Question',
              name: f.q,
              acceptedAnswer: { '@type': 'Answer', text: f.a },
            })),
          }),
        }}
      />
    </div>
  );
}
