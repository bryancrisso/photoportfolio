import Link from 'next/link';

export default function Navbar() {
  return (
    <div>
      <nav className="bg-white p-4">
        <div className="container mx-2 flex justify-between items-center">
          <Link href="/" className="text-black font-bold text-xl">
            brizzle.ography
          </Link>
        </div>
      </nav>
    </div>
  );
}
