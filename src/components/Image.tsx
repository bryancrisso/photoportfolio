export default function Image({ filepath }: { filepath: string }) {
  return (
    <img
      src={filepath}
      className={`shrink-0 object-contain rounded-md 
                  drop-shadow-md transition-all duration-300 
                  hover:drop-shadow-xl hover:scale-[1.005]`}
    />
  )
}
