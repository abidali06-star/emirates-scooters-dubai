// Next.js App Router Root Layout Server Component (app/layout.tsx)
import React from 'react';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  metadataBase: new URL('https://emirates-scooters-dubai.vercel.app'),
  title: {
    default: 'Emirates E-Scooters | Mankeel Electric Scooters Delivered Across Dubai',
    template: '%s | Emirates E-Scooters',
  },
  description: 'Mankeel MK083 and MX-14 electric scooters delivered across Dubai. One-year warranty, battery servicing, and free local delivery to Motor City, Sports City, JVC, Arabian Ranches, Damac Hills, Mudon, Studio City, Al Barsha South, Production City, Green Community, and JVT.',
  keywords: [
    'Mankeel Dubai',
    'Mankeel electric scooter UAE',
    'buy e-scooter Dubai',
    'best electric scooter Dubai',
    'Xiaomi e scooter alternative Dubai',
    'Ninebot alternative UAE',
    'Mankeel vs Xiaomi Dubai',
    'good quality electric scooter Dubai',
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
    title: 'Emirates E-Scooters | Mankeel Electric Scooters Delivered Across Dubai',
    description: 'Buy Mankeel electric scooters in Dubai, delivered to you. In-stock models from 699 AED with free local delivery.',
    images: [
      {
        url: 'https://emirates-scooters-dubai.vercel.app/Images/MK083.png',
        width: 1200,
        height: 630,
        alt: 'Mankeel electric scooters delivered across Dubai',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Emirates E-Scooters | Mankeel Scooters, Dubai',
    description: 'Mankeel electric scooters delivered across Dubai. Free local delivery.',
    images: ['https://emirates-scooters-dubai.vercel.app/Images/MK083.png'],
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
  // Service area business: no premises open to the public. Per Google's
  // structured-data guidance for service-area businesses, streetAddress and geo
  // are omitted and areaServed carries the coverage instead. Do not add a
  // street address back - the business has no public location.
  const localBusinessSchema = {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    name: 'Emirates E-Scooters',
    image: 'https://emirates-scooters-dubai.vercel.app/Images/MK083.png',
    telephone: '+971 56 667 2354',
    url: 'https://emirates-scooters-dubai.vercel.app',
    sameAs: [
      'https://www.facebook.com/profile.php?id=61582981335703',
    ],
    address: {
      '@type': 'PostalAddress',
      addressLocality: 'Dubai',
      addressRegion: 'Dubai',
      addressCountry: 'AE',
    },
    areaServed: [
      'Motor City',
      'Sports City',
      'JVC',
      'Arabian Ranches',
      'Damac Hills',
      'Mudon',
      'Studio City',
      'Al Barsha South',
      'Production City',
      'Green Community',
      'JVT',
    ],
    // Contact and delivery hours, confirmed 2026-08-29. Not shop hours - there is no shop.
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
    priceRange: 'AED 699 - AED 2299',
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
