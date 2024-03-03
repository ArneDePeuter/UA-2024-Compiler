// Generated from /Users/arne/Documents/repos/school/Compiler/src/antlr_files/project_1/MyGrammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MyGrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, NUMBER=4, PLUS=5, MINUS=6, MUL=7, DIV=8, MOD=9, 
		GT=10, LT=11, EQ=12, GE=13, LE=14, NE=15, AND=16, OR=17, NOT=18, LSHIFT=19, 
		RSHIFT=20, BITAND=21, BITOR=22, BITXOR=23, BITNOT=24, WS=25;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "NUMBER", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
			"GT", "LT", "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", 
			"BITAND", "BITOR", "BITXOR", "BITNOT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'('", "')'", null, "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
			"'<'", "'=='", "'>='", "'<='", "'!='", "'&&'", "'||'", "'!'", "'<<'", 
			"'>>'", "'&'", "'|'", "'^'", "'~'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "NUMBER", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
			"GT", "LT", "EQ", "GE", "LE", "NE", "AND", "OR", "NOT", "LSHIFT", "RSHIFT", 
			"BITAND", "BITOR", "BITXOR", "BITNOT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public MyGrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MyGrammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0019z\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003=\b"+
		"\u0003\n\u0003\f\u0003@\t\u0003\u0003\u0003B\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0001\u0018\u0004\u0018u\b\u0018\u000b\u0018\f\u0018v\u0001\u0018"+
		"\u0001\u0018\u0000\u0000\u0019\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013"+
		"\'\u0014)\u0015+\u0016-\u0017/\u00181\u0019\u0001\u0000\u0003\u0001\u0000"+
		"19\u0001\u000009\u0003\u0000\t\n\r\r  |\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001"+
		"\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000"+
		"\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000"+
		"\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u00001"+
		"\u0001\u0000\u0000\u0000\u00013\u0001\u0000\u0000\u0000\u00035\u0001\u0000"+
		"\u0000\u0000\u00057\u0001\u0000\u0000\u0000\u0007A\u0001\u0000\u0000\u0000"+
		"\tC\u0001\u0000\u0000\u0000\u000bE\u0001\u0000\u0000\u0000\rG\u0001\u0000"+
		"\u0000\u0000\u000fI\u0001\u0000\u0000\u0000\u0011K\u0001\u0000\u0000\u0000"+
		"\u0013M\u0001\u0000\u0000\u0000\u0015O\u0001\u0000\u0000\u0000\u0017Q"+
		"\u0001\u0000\u0000\u0000\u0019T\u0001\u0000\u0000\u0000\u001bW\u0001\u0000"+
		"\u0000\u0000\u001dZ\u0001\u0000\u0000\u0000\u001f]\u0001\u0000\u0000\u0000"+
		"!`\u0001\u0000\u0000\u0000#c\u0001\u0000\u0000\u0000%e\u0001\u0000\u0000"+
		"\u0000\'h\u0001\u0000\u0000\u0000)k\u0001\u0000\u0000\u0000+m\u0001\u0000"+
		"\u0000\u0000-o\u0001\u0000\u0000\u0000/q\u0001\u0000\u0000\u00001t\u0001"+
		"\u0000\u0000\u000034\u0005;\u0000\u00004\u0002\u0001\u0000\u0000\u0000"+
		"56\u0005(\u0000\u00006\u0004\u0001\u0000\u0000\u000078\u0005)\u0000\u0000"+
		"8\u0006\u0001\u0000\u0000\u00009B\u00050\u0000\u0000:>\u0007\u0000\u0000"+
		"\u0000;=\u0007\u0001\u0000\u0000<;\u0001\u0000\u0000\u0000=@\u0001\u0000"+
		"\u0000\u0000><\u0001\u0000\u0000\u0000>?\u0001\u0000\u0000\u0000?B\u0001"+
		"\u0000\u0000\u0000@>\u0001\u0000\u0000\u0000A9\u0001\u0000\u0000\u0000"+
		"A:\u0001\u0000\u0000\u0000B\b\u0001\u0000\u0000\u0000CD\u0005+\u0000\u0000"+
		"D\n\u0001\u0000\u0000\u0000EF\u0005-\u0000\u0000F\f\u0001\u0000\u0000"+
		"\u0000GH\u0005*\u0000\u0000H\u000e\u0001\u0000\u0000\u0000IJ\u0005/\u0000"+
		"\u0000J\u0010\u0001\u0000\u0000\u0000KL\u0005%\u0000\u0000L\u0012\u0001"+
		"\u0000\u0000\u0000MN\u0005>\u0000\u0000N\u0014\u0001\u0000\u0000\u0000"+
		"OP\u0005<\u0000\u0000P\u0016\u0001\u0000\u0000\u0000QR\u0005=\u0000\u0000"+
		"RS\u0005=\u0000\u0000S\u0018\u0001\u0000\u0000\u0000TU\u0005>\u0000\u0000"+
		"UV\u0005=\u0000\u0000V\u001a\u0001\u0000\u0000\u0000WX\u0005<\u0000\u0000"+
		"XY\u0005=\u0000\u0000Y\u001c\u0001\u0000\u0000\u0000Z[\u0005!\u0000\u0000"+
		"[\\\u0005=\u0000\u0000\\\u001e\u0001\u0000\u0000\u0000]^\u0005&\u0000"+
		"\u0000^_\u0005&\u0000\u0000_ \u0001\u0000\u0000\u0000`a\u0005|\u0000\u0000"+
		"ab\u0005|\u0000\u0000b\"\u0001\u0000\u0000\u0000cd\u0005!\u0000\u0000"+
		"d$\u0001\u0000\u0000\u0000ef\u0005<\u0000\u0000fg\u0005<\u0000\u0000g"+
		"&\u0001\u0000\u0000\u0000hi\u0005>\u0000\u0000ij\u0005>\u0000\u0000j("+
		"\u0001\u0000\u0000\u0000kl\u0005&\u0000\u0000l*\u0001\u0000\u0000\u0000"+
		"mn\u0005|\u0000\u0000n,\u0001\u0000\u0000\u0000op\u0005^\u0000\u0000p"+
		".\u0001\u0000\u0000\u0000qr\u0005~\u0000\u0000r0\u0001\u0000\u0000\u0000"+
		"su\u0007\u0002\u0000\u0000ts\u0001\u0000\u0000\u0000uv\u0001\u0000\u0000"+
		"\u0000vt\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wx\u0001\u0000"+
		"\u0000\u0000xy\u0006\u0018\u0000\u0000y2\u0001\u0000\u0000\u0000\u0004"+
		"\u0000>Av\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}