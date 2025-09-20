import styles from "./ResultCard.module.css";

export default function ResultCard({ r, idx }) {
  const preview =
    (r.chunk ?? r.text ?? r.content ?? "").length > 800
      ? (r.chunk ?? r.text ?? r.content ?? "").slice(0, 800) + "..."
      : r.chunk ?? r.text ?? r.content ?? "";

  return (
    <div className={styles.card}>
      {/* Heading “No. x” */}
      <div className={styles.header}>No. {idx + 1}</div>

      <div className={styles.body}>
        <div className={styles.text}>{r.chunk ?? r.text ?? r.content}</div>
      </div>
    </div>
  );
}
