import styles from "./ResultCard.module.css";

export default function ResultCard({ r, idx }) {
  return (
    <div className={styles.card}>
      <div className={styles.header}>
        No. {idx + 1}
        {typeof r.score !== "undefined" && (
          <span className={styles.score}>
            Score: {Number(r.score).toFixed(3)}
          </span>
        )}
      </div>

      <div className={styles.body}>
        <div className={styles.text}>{r.chunk ?? r.text ?? r.content}</div>
      </div>
    </div>
  );
}
