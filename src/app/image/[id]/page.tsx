import Image from "@/src/components/Image"
import { ImageResult } from "@/src/types/image"
import { query } from "@/src/utils/db"


export default async function ImagePage({ params }: { params: { id: string } }) {
  const data = await query<ImageResult>("SELECT * FROM images WHERE image_id = $1", [params.id]);
  const image = data.rows[0];
  return (
    <div className="flex justify-center items-center h-[90vh]">
      <div className="grid grid-cols-3 gap-4">
        <div className="flex h-[90vh] w-[100vh] relative justify-end col-span-2">
          <Image filepath={"/" + image.filepath}></Image>
        </div>
        <div className="flex flex-col items-left justify-center p-8">
          <h1 className="text-2xl font-bold mb-4">Hi</h1>
          <p>Taken in France</p>
        </div>
      </div>
    </div>
  )
}

