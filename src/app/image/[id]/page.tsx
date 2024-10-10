import Image from "@/src/components/Image"
import { ImageResult } from "@/src/types/image"
import { query } from "@/src/utils/db"


export default async function ImagePage({ params }: { params: { id: string } }) {
  const data = await query<ImageResult>("SELECT * FROM images WHERE image_id = $1", [params.id]);
  const image = data.rows[0];
  return (
    <div className="flex w-full min-h-screen pr-4 pl-4 pb-4">
      <div className="w-3/4 pr-4">
        <div className="rounded-lg  shadow-lg h-[90vh]">
          <Image filepath={"/" + image.filepath}></Image>
        </div>
      </div>
      <div className="w-1/4 bg-yellow-50 p-6 rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold mb-4">Image Title</h2>
        <p className="text-gray-600 mb-4">
          This is a description of the image. You can include details about what the image represents,
          when it was taken, or any other relevant information.
        </p>
        <div className="space-y-2">
          <p className="text-sm">
            <span className="font-semibold">Date:</span> October 8, 2024
          </p>
          <p className="text-sm">
            <span className="font-semibold">Location:</span> Sample Location
          </p>
          <p className="text-sm">
            <span className="font-semibold">Photographer:</span> John Doe
          </p>
        </div>
      </div>
    </div>
  )
}

