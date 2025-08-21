import ProductList from '@/components/ProductList'

export default function ProductsPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="text-center mb-12">
        <h1 className="text-4xl font-bold text-brand mb-4">Товары</h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Выберите необходимое оборудование для вашего проекта
        </p>
      </div>
      <ProductList />
    </div>
  )
} 