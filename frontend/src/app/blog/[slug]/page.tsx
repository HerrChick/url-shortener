export default function BlogPost({ params }: { params: { slug: string } }) {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20">
      <h1 className="text-4xl font-bold">Blog Post: {params.slug}</h1>
      <p className="text-lg">This is a dynamic blog post page.</p>
    </div>
  );
} 