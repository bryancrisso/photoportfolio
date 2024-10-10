export default function Image({ filepath }: { filepath: string }) {
  return (
    <img
      src={filepath}
      className={"absolute inset-0 w-full h-full object-contain"}
      style={{
        position: 'relative',
        width: '100%',
      }}
    />
  )
}
