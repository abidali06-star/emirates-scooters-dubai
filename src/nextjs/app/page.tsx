import React from 'react';
import Link from 'next/link';

export default function HomePage() {
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
          Official Dubai catalog of Mankeel electric scooters, with local summer warranty and fast delivery across Motor City, Sports City, and JVC.
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

      <section className="bg-emerald-50 p-6 rounded-xl border border-emerald-200">
        <h2 className="text-xl font-bold text-emerald-900 mb-2">Dubai Local Authority Hub & RTA Compliance</h2>
        <ul className="space-y-2 text-emerald-800 text-sm font-medium">
          <li>• <strong>RTA Permit Guide:</strong> How to obtain your free Dubai e-scooter permit online.</li>
          <li>• <strong>Summer Heat Care:</strong> Protecting lithium batteries in 45°C+ UAE summer heat.</li>
          <li>• <strong>Track Maps:</strong> Designated tracks in JLT, Dubai Water Canal, Business Bay & Downtown Dubai.</li>
        </ul>
      </section>
    </div>
  );
}
