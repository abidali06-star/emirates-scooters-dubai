// Next.js App Router Root Layout Server Component (app/layout.tsx)
import React from 'react';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  metadataBase: new URL('https://emirates-scooters.ae'),
  title: {
    default: 'Mankeel E-Scooters Dubai | Official Store & RTA Authorized Dealer',
    template: '%s | Mankeel E-Scooters Dubai',
  },
  description: 'Official Dubai store for Mankeel MX-14, MX-14, MX25, MK083, and MK085 electric scooters. RTA compliant, summer battery warranty, local delivery in JLT, Marina, Business Bay.',
  keywords: [
    'Mankeel Dubai',
    'Mankeel electric scooter UAE',
    'RTA compliant e-scooter',
    'Mankeel MX-14',
    'Mankeel MX-14',
    'Mankeel MX25',
    'Mankeel MK083',
    'Mankeel MK085',
    'e-scooter Dubai price',
    'electric scooter JLT Marina',
  ],
  authors: [{ name: 'Emirates Scooters Dubai' }],
  creator: 'Mankeel E-Scooters Dubai',
  openGraph: {
    type: 'website',
    locale: 'en_AE',
    url: 'https://emirates-scooters.ae',
    siteName: 'Mankeel E-Scooters Dubai',
    title: 'Mankeel E-Scooters Dubai | Official Store & RTA Authorized Dealer',
    description: 'Buy official RTA-compliant Mankeel electric scooters in Dubai. In-stock models starting from 699 AED with free Dubai delivery.',
    images: [
      {
        url: 'https://emirates-scooters.ae/images/og-mankeel-dubai.jpg',
        width: 1200,
        height: 630,
        alt: 'Mankeel Electric Scooters Dubai Showroom',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mankeel E-Scooters Dubai | Official Store',
    description: 'Official Mankeel electric scooters in Dubai. RTA-compliant 25 km/h models.',
    images: ['https://emirates-scooters.ae/images/og-mankeel-dubai.jpg'],
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
    name: 'Mankeel E-Scooters Dubai',
    image: 'https://emirates-scooters.ae/images/storefront-jlt.jpg',
    telephone: '+971 4 456 7890',
    url: 'https://emirates-scooters.ae',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Store 14, Ground Floor, Silver Tower, Cluster I, Jumeirah Lakes Towers (JLT)',
      addressLocality: 'Dubai',
      addressRegion: 'Dubai',
      postalCode: '00000',
      addressCountry: 'AE',
    },
    geo: {
      '@type': 'GeoCoordinates',
      latitude: 25.07725,
      longitude: 55.15012,
    },
    priceRange: 'AED 699 - AED 2299',
    openingHoursSpecification: [
      {
        '@type': 'OpeningHoursSpecification',
        dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
        opens: '09:00',
        closes: '21:00',
      },
    ],
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
