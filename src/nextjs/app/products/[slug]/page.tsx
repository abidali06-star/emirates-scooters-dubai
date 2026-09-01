// Dynamic Next.js App Router Product Page Server Component (app/products/[slug]/page.tsx)
import React from 'react';
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import productsData from '@/lib/data/products.json';

interface ProductItem {
  Model: string;
  slug: string;
  name: string;
  "Price AED": number;
  Stock: string;
  inStock: boolean;
  "Product Link": string;
  image: string | null;
  specifications: {
    "Top Speed": string;
    Range: string;
    Motor: string;
    Battery: string;
    Tire: string;
    "Charge time": string;
    Weight: string;
    "Max Load": string;
  };
  key_features: string[];
}

export async function generateMetadata({ params }: { params: { slug: string } }): Promise<Metadata> {
  const slug = params.slug.toLowerCase();
  const product = productsData.find((p) => p.slug.toLowerCase() === slug) as ProductItem | undefined;

  if (!product) {
    return {
      title: 'Product Not Found',
    };
  }

  const title = `Mankeel ${product.Model} Electric Scooter Dubai | ${product['Price AED']} AED`;
  const description = `Buy official Mankeel ${product.Model} in Dubai. Motor: ${product.specifications.Motor}, Top Speed: ${product.specifications['Top Speed']}, Range: ${product.specifications.Range}. ${product.inStock ? 'In Stock with Fast Dubai Delivery.' : 'Currently Out of Stock.'}`;

  return {
    title,
    description,
    alternates: {
      canonical: `https://emirates-scooters-dubai.vercel.app/products/${product.slug}`,
    },
    openGraph: {
      title,
      description,
      url: `https://emirates-scooters-dubai.vercel.app/products/${product.slug}`,
      images: product.image
        ? [
            {
              url: `https://emirates-scooters-dubai.vercel.app${product.image}`,
              width: 800,
              height: 600,
              alt: `Mankeel ${product.Model} Electric Scooter`,
            },
          ]
        : [],
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
      images: product.image ? [`https://emirates-scooters-dubai.vercel.app${product.image}`] : [],
    },
  };
}

export default async function ProductPage({ params }: { params: { slug: string } }) {
  const slug = params.slug.toLowerCase();
  const product = productsData.find((p) => p.slug.toLowerCase() === slug) as ProductItem | undefined;

  if (!product) {
    notFound();
  }

  // Per-product FAQ schema. These are the questions buyers actually ask, so they
  // give AI engines and Google direct answers tied to this specific model.
  const faqs = [
    {
      q: `Is the Mankeel ${product.Model} legal to ride in Dubai?`,
      a: `Yes, on designated tracks and shared paths with a free RTA permit. RTA requires an e-scooter's maximum speed to be set to 20 km/h, and this model has three speed modes with mode 1 limited to 20 km/h.`,
    },
    {
      q: `How far does the Mankeel ${product.Model} go on one charge?`,
      a: `Rated ${product.specifications.Range} per charge. Expect roughly 70-80% of that in Dubai summer heat, depending on rider weight, speed mode and terrain.`,
    },
    {
      q: `How long does the Mankeel ${product.Model} take to charge?`,
      a: `${product.specifications['Charge time']}. Let the battery cool for 30-45 minutes indoors before charging after a ride.`,
    },
    {
      q: `How much does the Mankeel ${product.Model} weigh?`,
      a: `${product.specifications.Weight}, carrying up to ${product.specifications['Max Load']}.`,
    },
    {
      q: `Do you deliver the Mankeel ${product.Model} in Dubai?`,
      a: `Yes. Free delivery across Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community and JVT. We hand it over in person so you can inspect it before you accept it.`,
    },
    {
      q: `Is there a warranty on the Mankeel ${product.Model}?`,
      a: `One year in the UAE, plus servicing and genuine Mankeel spare parts held locally.`,
    },
  ];

  const faqSchema = {
    '@context': 'https://schema.org',
    '@type': 'FAQPage',
    mainEntity: faqs.map((f) => ({
      '@type': 'Question',
      name: f.q,
      acceptedAnswer: { '@type': 'Answer', text: f.a },
    })),
  };

  const productSchema = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: `Mankeel ${product.Model}`,
    image: product.image ? `https://emirates-scooters-dubai.vercel.app${product.image}` : undefined,
    description: `Official Mankeel ${product.Model} electric scooter in Dubai featuring a ${product.specifications.Motor} motor and top speed of ${product.specifications['Top Speed']}. Range: ${product.specifications.Range}.`,
    sku: `MNK-${product.Model.replace('-', '')}-DXB`,
    brand: {
      '@type': 'Brand',
      name: 'Mankeel',
    },
    offers: {
      '@type': 'Offer',
      priceCurrency: 'AED',
      price: product['Price AED'],
      availability: product.inStock
        ? 'https://schema.org/InStock'
        : 'https://schema.org/OutOfStock',
      seller: {
        '@type': 'Organization',
        name: 'Emirates E-Scooters',
      },
    },
  };

  return (
    <article className="max-w-4xl mx-auto p-6">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(productSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(faqSchema) }}
      />
      
      <header className="mb-6 flex flex-col md:flex-row md:items-center justify-between border-b pb-4">
        <div>
          <div className="flex items-center gap-3">
            <span className="text-sm font-semibold text-slate-500">Mankeel Series</span>
            {product.inStock ? (
              <span className="bg-emerald-500 text-white text-xs px-3 py-1 rounded-full font-bold">
                In Stock
              </span>
            ) : (
              <span className="bg-rose-500 text-white text-xs px-3 py-1 rounded-full font-bold">
                Out of Stock
              </span>
            )}
          </div>
          <h1 className="text-3xl font-bold mt-2 text-slate-900">Mankeel {product.Model}</h1>
        </div>
        <div className="mt-4 md:mt-0 text-right">
          <div className="text-3xl font-extrabold text-blue-600">
            {product['Price AED']} AED
          </div>
          <p className="text-xs text-slate-500 mt-1">VAT Included</p>
        </div>
      </header>

      {/* Specifications Table */}
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-4 text-slate-800">Technical Specifications</h2>
        <div className="overflow-x-auto">
          <table className="w-full border-collapse bg-white border border-slate-200 rounded-lg shadow-sm">
            <thead>
              <tr className="bg-slate-900 text-white">
                <th className="p-3 text-left">Specification Parameter</th>
                <th className="p-3 text-left">Engineered Detail</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-200">
              <tr><td className="p-3 font-medium text-slate-700">Top Speed</td><td className="p-3 text-slate-900">{product.specifications['Top Speed']}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Maximum Range</td><td className="p-3 text-slate-900">{product.specifications.Range}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Motor Output</td><td className="p-3 text-slate-900">{product.specifications.Motor}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Battery Specs</td><td className="p-3 text-slate-900">{product.specifications.Battery}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Tire Specification</td><td className="p-3 text-slate-900">{product.specifications.Tire}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Charging Duration</td><td className="p-3 text-slate-900">{product.specifications['Charge time']}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Scooter Weight</td><td className="p-3 text-slate-900">{product.specifications.Weight}</td></tr>
              <tr><td className="p-3 font-medium text-slate-700">Maximum Payload</td><td className="p-3 text-slate-900">{product.specifications['Max Load']}</td></tr>
            </tbody>
          </table>
        </div>
      </section>

      {/* Key Features List */}
      <section className="mb-8 bg-white p-6 rounded-lg border border-slate-200 shadow-sm">
        <h2 className="text-xl font-semibold mb-4 text-slate-800">Key Features</h2>
        <ul className="list-disc pl-5 space-y-2 text-slate-700">
          {product.key_features.map((feature, idx) => (
            <li key={idx} className="font-medium">{feature}</li>
          ))}
        </ul>
      </section>

      {/* Order Actions */}
      <section className="flex items-center justify-between bg-slate-100 p-6 rounded-lg">
        <div>
          <p className="font-semibold text-slate-800">Ready to Order in Dubai?</p>
          <p className="text-sm text-slate-600">Free delivery across Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community, and JVT.</p>
        </div>
        {product.inStock ? (
          <a
            href={product['Product Link']}
            target="_blank"
            rel="noopener noreferrer"
            className="bg-blue-600 text-white font-bold px-6 py-3 rounded-lg hover:bg-blue-700 transition"
          >
            Buy Now ({product['Price AED']} AED)
          </a>
        ) : (
          <button
            disabled
            className="bg-slate-400 text-white font-bold px-6 py-3 rounded-lg cursor-not-allowed"
          >
            Out of Stock
          </button>
        )}
      </section>
      <section className="mt-10 rounded-lg border border-slate-200 bg-slate-50 p-5">
          <h2 className="mb-3 text-lg font-bold text-slate-900">
            Mankeel {product.Model} &mdash; common questions
          </h2>
          {faqs.map((f, i) => (
            <div key={i} className="mb-3">
              <p className="text-sm font-semibold text-slate-900">{f.q}</p>
              <p className="text-sm text-slate-700">{f.a}</p>
            </div>
          ))}
        </section>
  
      </article>
  );
}
