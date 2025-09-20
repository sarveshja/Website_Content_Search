// components/InputField.jsx
import styles from "./InputField.module.css";

export default function InputField({ type, placeholder, value, onChange }) {
  return (
    <div className={styles.field}>
      <input
        type={type}
        className={styles.input}
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        required
      />
    </div>
  );
}
