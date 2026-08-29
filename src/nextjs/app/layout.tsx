// Next.js App Router Root Layout Server Component (app/layout.tsx)
import React from 'react';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  metadataBase: new URL('https://emirates-scooters-dubai.vercel.app'),
  title: {
    default: 'Emirates E-Scooters | Official Store & RTA Authorized Dealer',
    template: '%s | Emirates E-Scooters',
  },
  description: 'Official Dubai store for Mankeel MK083 and MX-14 electric scooters. RTA compliant, summer battery warranty, local delivery in Motor City, Sports City, and JVC.',
  keywords: [
    'Mankeel Dubai',
    'Mankeel electric scooter UAE',
    'RTA compliant e-scooter',
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
    title: 'Emirates E-Scooters | Official Store & RTA Authorized Dealer',
    description: 'Buy official RTA-compliant Mankeel electric scooters in Dubai. In-stock models starting from 699 AED with free Dubai delivery.',
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
    description: 'Official Mankeel electric scooters in Dubai. RTA-compliant models.',
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
    // NOTE: priceRange and openingHoursSpecification are deliberately omitted.
    // The previous values (AED 699-2299, 09:00-21:00) were placeholders that had
    // never been confirmed by the owner. An absent field is harmless; a wrong one
    // becomes a permanent citation that Google and AI engines will repeat.
    // Add them back only once the real trading hours and price range are known.
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
