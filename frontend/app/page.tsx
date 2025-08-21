import ProductsSlider from '@/components/ProductsSlider'

export default function HomePage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <section className="text-center mb-16">
        <h1 className="text-4xl font-bold text-brand mb-6">NartRental</h1>
        <p className="text-lg text-gray-600 max-w-3xl mx-auto leading-relaxed">
          Мы предоставляем профессиональное оборудование для съемок, мероприятий и проектов. 
          Наша миссия - сделать качественное оборудование доступным для творческих профессионалов.
        </p>
      </section>

      <div className="bg-gradient-to-r from-gray-200 via-gray-100 to-gray-200 py-12 mb-16">
        <div className="text-center">
          <div className="inline-block bg-white px-8 py-4 rounded-lg shadow-sm">
            <span className="text-xl text-gray-600 font-medium">
              NartRental • Аренда оборудования • Профессиональные решения
            </span>
          </div>
        </div>
      </div>

      <section className="mb-16">
        <h2 className="text-3xl font-bold text-center mb-8">Наша мотивация</h2>
        <div className="max-w-4xl mx-auto space-y-6">
          <p className="text-lg text-gray-700 leading-relaxed">
            Мы понимаем, что качественное оборудование - это основа успешного проекта. 
            Поэтому мы тщательно отбираем каждую единицу техники и поддерживаем её в отличном состоянии.
          </p>
          <p className="text-lg text-gray-700 leading-relaxed">
            Наша команда состоит из профессионалов, которые знают специфику работы с оборудованием 
            и готовы помочь в выборе оптимального решения для ваших задач.
          </p>
        </div>
      </section>

      <section>
        <h2 className="text-3xl font-bold text-center mb-8">Товары</h2>
        <ProductsSlider />
      </section>
    </div>
  )
} 