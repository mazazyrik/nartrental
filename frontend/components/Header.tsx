import Link from 'next/link'
import Image from 'next/image'

export default function Header() {
  return (
    <header>
      <div className="bg-brand h-1"></div>
      <div className="container mx-auto px-4 py-6">
        <div className="text-center mb-6">
          <Link href="/" className="inline-block">
            <Image
              src="/images/logo.jpeg"
              alt="NartRental"
              width={200}
              height={80}
              className="mx-auto hover:opacity-90 transition-opacity"
              priority
            />
          </Link>
        </div>
        <nav className="flex justify-center space-x-4">
          <Link href="/" className="btn-secondary">
            Главная
          </Link>
          <Link href="/products" className="btn-secondary">
            Товары
          </Link>
        </nav>
      </div>
    </header>
  )
} 