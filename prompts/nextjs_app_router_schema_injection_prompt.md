# Antigravity Prompt: Next.js App Router JSON-LD Schema Injection

**Role & Objective:**
You are an expert Next.js and SEO developer. Your task is to inject machine-readable JSON-LD structured data into this repository using Next.js App Router (Server Components) standards.

**Task 1: Global LocalBusiness Schema (app/layout.tsx)**
1. Locate `app/layout.tsx`.
2. Generate a JSON-LD `LocalBusiness` object for "Emirates E-Scooters".
3. Include the following precise properties:
   - `@context`: "https://schema.org"
   - `@type`: "LocalBusiness"
   - `name`: "Emirates E-Scooters"
   - `image`: "https://emirates-scooters-dubai.vercel.app/images/storefront-jlt.jpg"
   - `telephone`: "+97144567890"
   - `address`: { "@type": "PostalAddress", "streetAddress": "Store 001, Waitrose, Motor City", "addressLocality": "Dubai", "addressCountry": "AE" }
   - `priceRange`: "AED 1399 - AED 2299"
4. Inject this object into the layout wrapper using a standard `<script type="application/ld+json">` tag with `dangerouslySetInnerHTML`. Ensure `JSON.stringify()` is used to parse the object. Do not use the `next/script` component.

**Task 2: Dynamic Product Schema (app/products/[slug]/page.tsx)**
1. Locate the dynamic product route (e.g., `app/products/[slug]/page.tsx`).
2. Map the fetched Next.js product data (name, description, price, image, stock status) into a `Product` JSON-LD object.
3. Ensure the schema includes an `offers` property containing:
   - `@type`: "Offer"
   - `priceCurrency`: "AED"
   - `price`: [Map to dynamic VAT-inclusive price variable]
   - `availability`: "https://schema.org/InStock" or "https://schema.org/OutOfStock"
4. Output the schema securely using a `<script>` tag with `dangerouslySetInnerHTML` directly in the Server Component's return statement alongside the UI elements.

```tsx
// Example app/layout.tsx implementation
export default function RootLayout({ children }: { children: React.ReactNode }) {
  const localBusinessSchema = {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    name: 'Emirates E-Scooters',
    image: 'https://emirates-scooters-dubai.vercel.app/images/storefront-jlt.jpg',
    telephone: '+97144567890',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Store 001, Waitrose, Motor City',
      addressLocality: 'Dubai',
      addressCountry: 'AE',
    },
    priceRange: 'AED 1399 - AED 2299',
  };

  return (
    <html lang="en">
      <body>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(localBusinessSchema) }}
        />
        {children}
      </body>
    </html>
  );
}
```

```tsx
// Example app/products/[slug]/page.tsx implementation
export default async function ProductPage({ params }: { params: { slug: string } }) {
  const product = await getProduct(params.slug);

  const productSchema = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.name,
    image: product.image,
    description: product.description,
    offers: {
      '@type': 'Offer',
      priceCurrency: 'AED',
      price: product.price,
      availability: product.inStock 
        ? 'https://schema.org/InStock' 
        : 'https://schema.org/OutOfStock',
    },
  };

  return (
    <section>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(productSchema) }}
      />
      <h1>{product.name}</h1>
    </section>
  );
}
```
