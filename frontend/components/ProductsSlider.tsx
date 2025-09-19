'use client'

import { useState, useEffect } from 'react'
import Image from 'next/image'

interface Product {
  id: number
  title: string
  image: string
  section?: 'caravan' | 'svetobaza' | 'locations'
}

export default function ProductsSlider() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch('/api/products/')
      .then(res => res.json())
      .then(data => {
        setProducts(data.results?.slice(0, 8) || [])
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [])

  const scrollLeft = () => {
    const container = document.getElementById('products-slider')
    if (container) {
      container.scrollBy({ left: -400, behavior: 'smooth' })
    }
  }

  const scrollRight = () => {
    const container = document.getElementById('products-slider')
    if (container) {
      container.scrollBy({ left: 400, behavior: 'smooth' })
    }
  }

  if (loading) {
    return (
      <div className="text-center py-12">
        <div className="inline-block animate-spin rounded-full h-10 w-10 border-b-2 border-brand"></div>
        <p className="mt-4 text-gray-600">Загрузка товаров...</p>
      </div>
    )
  }

  if (products.length === 0) {
    return (
      <div className="text-center py-12 text-gray-500">
        Товары не найдены
      </div>
    )
  }

  return (
    <div className="relative max-w-6xl mx-auto">
      <button
        onClick={scrollLeft}
        className="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-3 rounded-full z-10 hover:bg-gray-700 transition-colors shadow-lg"
        aria-label="Прокрутить влево"
      >
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
      </button>
      
      <div
        id="products-slider"
        className="flex space-x-6 overflow-x-auto scrollbar-hide px-16 py-4"
        style={{ scrollbarWidth: 'none', msOverflowStyle: 'none' }}
      >
        {products.map((product) => (
          <div key={product.id} className="flex-shrink-0 w-72">
            <div className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow duration-300">
              <div className="relative h-56">
                <Image
                  src={(product.image as any).startsWith('http') ? (product.image as any) : ((product.image as any).startsWith('/') ? (product.image as any) : `/media/${product.image}`)}
                  alt={product.title}
                  fill
                  className="object-cover hover:scale-105 transition-transform duration-300"
                  loading="lazy"
                />
              </div>
              <div className="p-4">
                <h4 className="font-semibold text-gray-800 truncate">{product.title}</h4>
              </div>
            </div>
          </div>
        ))}
      </div>

      <button
        onClick={scrollRight}
        className="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-3 rounded-full z-10 hover:bg-gray-700 transition-colors shadow-lg"
        aria-label="Прокрутить вправо"
      >
        <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
        </svg>
      </button>
    </div>
  )
} 