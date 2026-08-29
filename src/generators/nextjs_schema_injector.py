"""
Module: nextjs_schema_injector.py
Implements Next.js App Router Server Component JSON-LD Schema Generator & Template Output.
Includes dynamic generateMetadata for OpenGraph, Twitter Cards, and SEO/GEO indexing.
Covers the Mankeel models present in data/mankeel_products.json (currently MK083, MX-14).
"""

import os
import json
from typing import Dict, Any

class NextJSSchemaInjector:
    def __init__(self, profile_path: str = "data/dubai_gbp_profile.json",
                 products_path: str = "data/mankeel_products.json"):
        with open(profile_path, "r", encoding="utf-8") as f:
            self.profile = json.load(f)
        with open(products_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)

    def _price_range(self) -> str:
        """Derived from the real catalogue so it can never contradict the products."""
        prices = [p["price_aed"] for p in self.products]
        return f"AED {min(prices)} - AED {max(prices)}"

    def generate_root_layout_tsx(self) -> str:
        nap = self.profile["nap_data"]
        b_name = self.profile["business_name"]["en"]
        price_range = self._price_range()

        tsx_content = f"""// Next.js App Router Root Layout Server Component (app/layout.tsx)
import React from 'react';
import type {{ Metadata }} from 'next';

export const metadata: Metadata = {{
  metadataBase: new URL('https://emirates-scooters-dubai.vercel.app'),
  title: {{
    default: 'Emirates E-Scooters | Mankeel Electric Scooters, Motor City Dubai',
    template: '%s | Emirates E-Scooters',
  }},
  description: 'Mankeel MK083 and MX-14 electric scooters in Dubai. One-year warranty, summer battery servicing, and local delivery across Motor City, Sports City and JVC.',
  keywords: [
    'Mankeel Dubai',
    'Mankeel electric scooter UAE',
    'e-scooter shop Dubai',
    'Mankeel MK083',
    'Mankeel MX-14',
    'e-scooter Dubai price',
    'electric scooter Motor City Dubai',
  ],
  authors: [{{ name: 'Emirates E-Scooters' }}],
  creator: 'Emirates E-Scooters',
  openGraph: {{
    type: 'website',
    locale: 'en_AE',
    url: 'https://emirates-scooters-dubai.vercel.app',
    siteName: 'Emirates E-Scooters',
    title: 'Emirates E-Scooters | Mankeel Electric Scooters, Motor City Dubai',
    description: 'Buy Mankeel electric scooters in Dubai. In-stock models from 699 AED with free local delivery.',
    images: [
      {{
        url: 'https://emirates-scooters-dubai.vercel.app/images/og-mankeel-dubai.jpg',
        width: 1200,
        height: 630,
        alt: 'Emirates E-Scooters showroom, Motor City Dubai',
      }},
    ],
  }},
  twitter: {{
    card: 'summary_large_image',
    title: 'Emirates E-Scooters | Official Store',
    description: 'Mankeel electric scooters in Dubai. Visit our Motor City store.',
    images: ['https://emirates-scooters-dubai.vercel.app/images/og-mankeel-dubai.jpg'],
  }},
  robots: {{
    index: true,
    follow: true,
    googleBot: {{
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    }},
  }},
}};

export default function RootLayout({{ children }}: {{ children: React.ReactNode }}) {{
  const localBusinessSchema = {{
    '@context': 'https://schema.org',
    '@type': 'Store',
    name: '{b_name}',
    image: 'https://emirates-scooters-dubai.vercel.app/images/storefront-motor-city.jpg',
    telephone: '{nap["phone"]}',
    url: 'https://emirates-scooters-dubai.vercel.app',
    address: {{
      '@type': 'PostalAddress',
      streetAddress: '{nap["store_number"]}, {nap["building_name"]}, {nap["area"]}',
      addressLocality: '{nap["city"]}',
      addressRegion: '{nap["emirate"]}',
      addressCountry: 'AE',
    }},
    geo: {{
      '@type': 'GeoCoordinates',
      latitude: {nap["geo_coordinates"]["latitude"]},
      longitude: {nap["geo_coordinates"]["longitude"]},
    }},
    // Hours confirmed by the owner 2026-08-29: 08:00-22:00, all seven days.
    openingHoursSpecification: [
      {{
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: [
          'Monday', 'Tuesday', 'Wednesday', 'Thursday',
          'Friday', 'Saturday', 'Sunday',
        ],
        opens: '08:00',
        closes: '22:00',
      }},
    ],
    // priceRange derived from the live catalogue, not hand-written, so it cannot
    // drift from the products actually on sale.
    priceRange: '{price_range}',
  }};

  return (
    <html lang="en">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{{{ __html: JSON.stringify(localBusinessSchema) }}}}
        />
        <main className="min-h-screen bg-slate-50">
          {{children}}
        </main>
      </body>
    </html>
  );
}}
"""
        return tsx_content

    def generate_product_page_tsx(self) -> str:
        tsx_content = """// Dynamic Next.js App Router Product Page Server Component (app/products/[slug]/page.tsx)
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
      images: [
        {
          url: `https://emirates-scooters-dubai.vercel.app/images/products/${product.slug}.jpg`,
          width: 800,
          height: 600,
          alt: `Mankeel ${product.Model} Electric Scooter`,
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
      images: [`https://emirates-scooters-dubai.vercel.app/images/products/${product.slug}.jpg`],
    },
  };
}

export default async function ProductPage({ params }: { params: { slug: string } }) {
  const slug = params.slug.toLowerCase();
  const product = productsData.find((p) => p.slug.toLowerCase() === slug) as ProductItem | undefined;

  if (!product) {
    notFound();
  }

  const productSchema = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: `Mankeel ${product.Model}`,
    image: `https://emirates-scooters-dubai.vercel.app/images/products/${product.slug}.jpg`,
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
          <p className="text-sm text-slate-600">Free delivery across Motor City, Sports City, and JVC.</p>
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
    </article>
  );
}
"""
        return tsx_content

    def export_nextjs_files(self, output_dir: str = "src/nextjs") -> Dict[str, str]:
        os.makedirs(f"{output_dir}/lib/data", exist_ok=True)
        os.makedirs(f"{output_dir}/app/products/[slug]", exist_ok=True)
        
        layout_path = f"{output_dir}/app/layout.tsx"
        product_page_path = f"{output_dir}/app/products/[slug]/page.tsx"
        
        with open(layout_path, "w", encoding="utf-8") as f:
            f.write(self.generate_root_layout_tsx())
            
        with open(product_page_path, "w", encoding="utf-8") as f:
            f.write(self.generate_product_page_tsx())
            
        return {
          "layout_tsx": layout_path,
          "product_page_tsx": product_page_path
        }

if __name__ == "__main__":
    injector = NextJSSchemaInjector()
    exported = injector.export_nextjs_files()
    print(f"Exported Next.js App Router Server Components:\n- {exported['layout_tsx']}\n- {exported['product_page_tsx']}")
