import InputField from "./InputField";
import styles from "./SearchForm.module.css";

export default function SearchForm({
  url,
  query,
  setUrl,
  setQuery,
  onSubmit,
  onReset,
  loading,
  error,
}) {
  return (
    <form className={styles.form} onSubmit={onSubmit}>
      <InputField
        type="url"
        placeholder="Website URL (https://example.com)"
        value={url}
        onChange={setUrl}
      />
      <InputField
        type="text"
        placeholder="Search query (e.g. pricing, login, contact)"
        value={query}
        onChange={setQuery}
      />

      <div className={styles.buttonRow}>
        <button type="submit" className={styles.btnPrimary} disabled={loading}>
          {loading ? "Searching..." : "Search"}
        </button>
        <button type="button" className={styles.btnSecondary} onClick={onReset}>
          Reset
        </button>
      </div>

      {error && <div className={styles.error}>{error}</div>}
    </form>
  );
}
