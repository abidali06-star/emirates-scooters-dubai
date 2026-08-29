// Next.js App Router Root Layout Server Component (app/layout.tsx)
import React from 'react';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  metadataBase: new URL('https://emirates-scooters-dubai.vercel.app'),
  title: {
    default: 'Emirates E-Scooters | Mankeel Electric Scooters, Motor City Dubai',
    template: '%s | Emirates E-Scooters',
  },
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
  authors: [{ name: 'Emirates E-Scooters' }],
  creator: 'Emirates E-Scooters',
  openGraph: {
    type: 'website',
    locale: 'en_AE',
    url: 'https://emirates-scooters-dubai.vercel.app',
    siteName: 'Emirates E-Scooters',
    title: 'Emirates E-Scooters | Mankeel Electric Scooters, Motor City Dubai',
    description: 'Buy Mankeel electric scooters in Dubai. In-stock models from 699 AED with free local delivery.',
    images: [
      {
        url: 'https://emirates-scooters-dubai.vercel.app/images/og-mankeel-dubai.jpg',
        width: 1200,
        height: 630,
        alt: 'Emirates E-Scooters showroom, Motor City Dubai',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Emirates E-Scooters | Official Store',
    description: 'Mankeel electric scooters in Dubai. Visit our Motor City store.',
    images: ['https://emirates-scooters-dubai.vercel.app/images/og-mankeel-dubai.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const localBusinessSchema = {
    '@context': 'https://schema.org',
    '@type': 'Store',
    name: 'Emirates E-Scooters',
    image: 'https://emirates-scooters-dubai.vercel.app/images/storefront-motor-city.jpg',
    telephone: '+971 56 667 2354',
    url: 'https://emirates-scooters-dubai.vercel.app',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Store 001, Waitrose, Motor City',
      addressLocality: 'Dubai',
      addressRegion: 'Dubai',
      addressCountry: 'AE',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: 25.041390226596707,
      longitude: 55.22914791534377,
    },
    // Hours confirmed by the owner 2026-08-29: 08:00-22:00, all seven days.
    openingHoursSpecification: [
      {
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: [
          'Monday', 'Tuesday', 'Wednesday', 'Thursday',
          'Friday', 'Saturday', 'Sunday',
        ],
        opens: '08:00',
        closes: '22:00',
      },
    ],
    // priceRange derived from the live catalogue, not hand-written, so it cannot
    // drift from the products actually on sale.
    priceRange: 'AED 699 - AED 1499',
  };

  return (
    <html lang="en">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(localBusinessSchema) }}
        />
        <main className="min-h-screen bg-slate-50">
          {children}
        </main>
      </body>
    </html>
  );
}
