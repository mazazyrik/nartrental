'use client'

import { useState, useEffect } from 'react'
import Image from 'next/image'
import OrderModal from './OrderModal'

interface Product {
  id: number
  title: string
  description: string
  price: number
  image: string
  section: 'caravan' | 'svetobaza' | 'locations'
}

export default function ProductList() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null)
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [section, setSection] = useState<'caravan' | 'svetobaza' | 'locations'>('caravan')

  useEffect(() => {
    const url = `/api/products/?section=${section}`
    fetch(url)
      .then(res => res.json())
      .then(data => {
        setProducts(data.results || [])
        setLoading(false)
      })
      .catch(() => setLoading(false))
  }, [section])

  const handleRent = (product: Product) => {
    setSelectedProduct(product)
    setIsModalOpen(true)
  }

  if (loading) {
    return (
      <div className="text-center py-16">
        <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-brand"></div>
        <p className="mt-4 text-gray-600">Загрузка товаров...</p>
      </div>
    )
  }

  return (
    <>
      <div className="flex justify-center gap-3 mb-10">
        <button
          onClick={() => setSection('caravan')}
          className={`px-6 py-2 rounded-full border ${section === 'caravan' ? 'bg-brand text-white border-brand' : 'bg-white text-gray-700 border-gray-300'}`}
        >
          Караван
        </button>
        <button
          onClick={() => setSection('svetobaza')}
          className={`px-6 py-2 rounded-full border ${section === 'svetobaza' ? 'bg-brand text-white border-brand' : 'bg-white text-gray-700 border-gray-300'}`}
        >
          Светобаза
        </button>
        <button
          onClick={() => setSection('locations')}
          className={`px-6 py-2 rounded-full border ${section === 'locations' ? 'bg-brand text-white border-brand' : 'bg-white text-gray-700 border-gray-300'}`}
        >
          Локации
        </button>
      </div>
      <div className="space-y-16">
        {products.map((product, index) => (
          <div
            key={product.id}
            className={`flex flex-col lg:flex-row gap-8 items-center ${
              index % 2 === 1 ? 'lg:flex-row-reverse' : ''
            }`}
          >
            <div className="w-full lg:w-1/2">
              <div className="relative h-80 lg:h-96 rounded-xl overflow-hidden shadow-lg">
                <Image
                  src={`/media${product.image}`}
                  alt={product.title}
                  fill
                  className="object-cover hover:scale-105 transition-transform duration-300"
                />
              </div>
            </div>
            
            <div className="w-full lg:w-1/2 text-center lg:text-left space-y-6">
              <h3 className="text-3xl font-bold text-brand leading-tight">
                {product.title}
              </h3>
              <p className="text-lg text-gray-600 leading-relaxed">
                {product.description}
              </p>
              <div className="text-3xl font-bold text-gray-800">
                {product.price / 100} ₽
              </div>
              <button
                onClick={() => handleRent(product)}
                className="bg-brand text-white px-10 py-4 rounded-lg hover:bg-blue-600 transition-colors text-lg font-semibold shadow-lg hover:shadow-xl transform hover:-translate-y-1"
              >
                Арендовать
              </button>
            </div>
          </div>
        ))}
      </div>

      {selectedProduct && (
        <OrderModal
          product={selectedProduct}
          isOpen={isModalOpen}
          onClose={() => {
            setIsModalOpen(false)
            setSelectedProduct(null)
          }}
        />
      )}
    </>
  )
} 