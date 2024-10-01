import styles from '@/src/components/styles.module.css'

export default function Image({ filepath }: { filepath: string }) {
  return (
    <img
      src={filepath}
      className={`w-1/5 h-auto rounded-md m-8
                  drop-shadow-md transition-all duration-300 
                  hover:drop-shadow-xl hover:scale-[1.02]`}
    />
  )
}
