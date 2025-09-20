import styles from "./Header.module.css";

export default function Header() {
  return (
    <header className={styles.header}>
      <h1 className={styles.title}>Website Content Search</h1>
      <p className={styles.subtitle}>
        Search through website content with precision
      </p>
    </header>
  );
}
